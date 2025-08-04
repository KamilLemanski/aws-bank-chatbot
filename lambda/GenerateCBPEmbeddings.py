import boto3
import json

s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

BUCKET = "cbp-chatbot-data-us"
INPUT_KEY = "CBP_chunks_all.json"
OUTPUT_KEY = "CBP_chunks_embedded.json"

def prepare_text(chunk):
    if chunk["source"] == "FAQ":
        return f"Pytanie: {chunk['question']}\nOdpowiedź: {chunk['answer']}"
    elif chunk["source"] == "Regulamin":
        return f"{chunk['paragraph']} {chunk['title']}\n{chunk['content']}"
    elif chunk["source"] == "Oferta":
        return f"{chunk['account_type']}\n{chunk['content']}"
    else:
        return json.dumps(chunk)

def get_embedding(text):
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps({"inputText": text}),
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response['body'].read())
    return result['embedding']

def lambda_handler(event, context):
    # Pobierz dane wejściowe z S3
    obj = s3.get_object(Bucket=BUCKET, Key=INPUT_KEY)
    chunks = json.loads(obj["Body"].read().decode("utf-8"))

    embedded_chunks = []
    for i, chunk in enumerate(chunks):
        text = prepare_text(chunk)
        embedding = get_embedding(text)
        embedded_chunks.append({
            "id": f"chunk_{i}",
            "text": text,
            "embedding": embedding,
            "metadata": chunk
        })

    # Zapisz wynik do S3
    s3.put_object(
        Bucket=BUCKET,
        Key=OUTPUT_KEY,
        Body=json.dumps(embedded_chunks, ensure_ascii=False, indent=2),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": f"Wygenerowano {len(embedded_chunks)} embeddingów i zapisano do {OUTPUT_KEY}"
    }
