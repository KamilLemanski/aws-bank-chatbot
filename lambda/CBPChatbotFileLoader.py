import boto3
import json
import re

s3 = boto3.client('s3')

BUCKET_NAME = 'cbp-chatbot-data-us'
FILES = {
    "CBP_FAQ.txt": "FAQ",
    "CBP_Oferta_Kont_Osobistych.txt": "Oferta",
    "CBP_Regulamin.txt": "Regulamin"
}

def chunk_faq(text):
    pattern = r"(Jak.*?)\n(Odp\.:.*?)\n(?=Jak|Czy|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    return [{"source": "FAQ", "question": q.strip(), "answer": a.strip()} for q, a in matches]

def chunk_oferta(text):
    oferta_chunks = []
    oferta_sections = re.split(r"\n\d+\.\s", text)
    for section in oferta_sections:
        if section.strip():
            lines = section.strip().split("\n")
            title = lines[0] if lines else "Nieznany typ konta"
            content = "\n".join(lines[1:]).strip()
            oferta_chunks.append({
                "source": "Oferta",
                "account_type": title,
                "content": content
            })
    return oferta_chunks

def chunk_regulamin(text):
    paragrafy = re.split(r"(?=\n§\s?\d+\.?)", text)
    chunks = []
    for p in paragrafy:
        match = re.match(r"\n§\s?(\d+\.?)\s?(.*)", p)
        if match:
            nr = match.group(1).strip()
            title = match.group(2).strip()
            content = p.strip()
            chunks.append({
                "source": "Regulamin",
                "paragraph": f"§ {nr}",
                "title": title,
                "content": content
            })
    return chunks

def lambda_handler(event, context):
    all_chunks = []

    for file_name, file_type in FILES.items():
        local_path = f"/tmp/{file_name}"
        try:
            s3.download_file(BUCKET_NAME, file_name, local_path)
            with open(local_path, 'r', encoding='utf-8') as f:
                text = f.read()

            if file_type == "FAQ":
                chunks = chunk_faq(text)
            elif file_type == "Oferta":
                chunks = chunk_oferta(text)
            elif file_type == "Regulamin":
                chunks = chunk_regulamin(text)
            else:
                chunks = []

            all_chunks.extend(chunks)
            print(f"{file_name}: podzielono na {len(chunks)} fragmentów.")

        except Exception as e:
            print(f"Błąd przy przetwarzaniu {file_name}: {e}")

    # Zapisz wynik jako JSON
    output_path = "/tmp/CBP_chunks_all.json"
    with open(output_path, 'w', encoding='utf-8') as out_file:
        json.dump(all_chunks, out_file, ensure_ascii=False, indent=2)

    # Wyślij plik do S3
    try:
        s3.upload_file(output_path, BUCKET_NAME, "CBP_chunks_all.json")
        print("Plik CBP_chunks_all.json został zapisany w S3.")
    except Exception as e:
        print(f"Błąd przy zapisie pliku JSON do S3: {e}")

    return {
        'statusCode': 200,
        'body': f"Gotowe. Podzielono {len(all_chunks)} fragmentów i zapisano jako JSON w S3."
    }
