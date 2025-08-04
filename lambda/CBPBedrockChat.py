import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    try:
        # Parsowanie wejścia
        body = json.loads(event.get("body", "{}"))
        user_input = body.get("message", "")
        print(">>> Otrzymane pytanie użytkownika:", user_input)

        # Inteligentne wyszukiwanie chunków (RAG)
        import math

        # Kosinusowe podobieństwo bez numpy
        def cosine_similarity(a, b):
            dot = sum(x * y for x, y in zip(a, b))
            norm_a = math.sqrt(sum(x * x for x in a))
            norm_b = math.sqrt(sum(y * y for y in b))
            if norm_a == 0 or norm_b == 0:
                return 0
            return dot / (norm_a * norm_b)

        # Ładowanie danych z S3
        s3 = boto3.client("s3")
        bucket = "cbp-chatbot-data-us"
        key = "CBP_chunks_embedded.json"

        s3_response = s3.get_object(Bucket=bucket, Key=key)
        chunks_data = json.loads(s3_response["Body"].read().decode("utf-8"))

        # Embedding zapytania przy pomocy Amazon Titan
        embedding_response = bedrock.invoke_model(
            modelId="amazon.titan-embed-text-v2:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({ "inputText": user_input })
        )

        # Parsowanie odpowiedzi
        embedding_body = json.loads(embedding_response["body"].read().decode("utf-8"))
        query_vector = embedding_body["embedding"]

        # Oblicz podobieństwo
        scored_chunks = []
        for item in chunks_data:
            if "embedding" in item and "text" in item:
                score = cosine_similarity(query_vector, item["embedding"])
                scored_chunks.append((score, item["text"]))

        # Top 5 chunków
        top_chunks = sorted(scored_chunks, reverse=True)[:5]
        retrieved_chunks = "\n".join([f"- {text}" for _, text in top_chunks])

        # Prompt
        prompt = f"""
Jesteś profesjonalnym chatbotem banku Concept Bank Polska (CBP). Twoim zadaniem jest odpowiadać po polsku, grzecznie i konkretnie na pytania klientów dotyczące:

- kont osobistych (Concept Basic, Concept Plus, Concept Student, Concept Młodzieżowe, Concept Premium),
- kart płatniczych,
- przelewów krajowych i zagranicznych,
- bankowości internetowej i mobilnej,
- opłat, prowizji, limitów oraz innych zasad działania banku.

Odpowiadaj:
- jak typowy chat bankowy (kulturalnie, miło, ale bez słów typu "Szanowna Pani" i "Szanowny Panie")
- przejrzyście – **stosuj numerowane listy, myślniki, akapity, łamanie linii `\n`**, ale **NIE używaj znaczników Markdown (`**`, `*`) ani pogrubień.**
- w **estetycznej i przejrzystej formie**
- używaj **akapitów, list wypunktowanych, wcięć i podziału na sekcje** (jak w profesjonalnej korespondencji bankowej)
- Ogranicz długość wypowiedzi do maksymalnie **150 słów**.

### Jeśli użytkownik zada pytanie **niezwiązane z bankiem**, CBP, finansami, produktami lub usługami bankowymi – NIE udzielaj odpowiedzi.  
W takim przypadku **zawsze odpowiedz tylko i wyłącznie tym zdaniem, bez wyjątku**:

**"Przepraszam, mogę udzielać odpowiedzi wyłącznie na pytania dotyczące banku Concept Bank Polska (CBP), jego oferty oraz usług finansowych."**

---

PYTANIE UŻYTKOWNIKA:
{user_input}

---

FRAGMENTY Z DOKUMENTÓW BANKU CBP:
{retrieved_chunks}

---

Twoja odpowiedź:
"""

        print(">>> Wysyłany prompt:\n", prompt)

        # Wywołanie Claude przez Bedrock
        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 1000
            })
        )

        # Parsowanie odpowiedzi z Claude'a
        response_body = response["body"].read().decode("utf-8")
        print(">>> Surowa odpowiedź modelu:\n", response_body)

        parsed = json.loads(response_body)
        answer = parsed.get("content", [{}])[0].get("text", "Brak odpowiedzi")

        print(">>> Finalna odpowiedź chatbota:", answer)

        # ✅ Prawidłowa struktura odpowiedzi JSON
        response_payload = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({ "reply": answer }, ensure_ascii=False),
            "isBase64Encoded": False
        }

        print(">>> Wysyłana odpowiedź do frontendu:", response_payload)

        return response_payload

    except Exception as e:
        print(">>> Błąd Lambda handlera:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({ "reply": f"[Błąd backendu]: {str(e)}" }, ensure_ascii=False),
            "isBase64Encoded": False
        }
