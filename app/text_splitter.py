from document_loader import load_pdf

def chunk_text(text, chunk_size, overlap):

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

test_text = "ABCDEFGHIJKL"
test_chunks = chunk_text(test_text, 4, 2)

print(test_chunks)

pages = load_pdf("data/Clase_2_Análisis_de_regresión.pdf")
document_chunks = []
for page in pages:
    page_text = page["text"]
    page_number = page["page_number"]
    page_chunks = chunk_text(page_text, 500, 100)

    for chunk_number, chunk in enumerate(page_chunks, start=1):
        chunk_data = {
            "page_number": page_number,
            "chunk_number": chunk_number,
            "text": chunk
    }
        document_chunks.append(chunk_data)

print(f"Total de chunks del documento: {len(document_chunks)}")  
print(document_chunks[-1])      
print(len(pages))

page_text = pages[1]["text"]

page_chunks = chunk_text(page_text, 500, 100)

print(f"Chunks creados: {len(page_chunks)}")

print(page_chunks[0])
print("\n--- CHUNK 2 ---\n")
print(page_chunks[1])

page_number = pages[1]["page_number"]
page_chunks_with_metadata = []
for chunk_number, chunk in enumerate(page_chunks, start=1):
    chunk_data = {
        "page_number": page_number,
        "chunk_number": chunk_number,
        "text": chunk
}
    page_chunks_with_metadata.append(chunk_data)


print(f"Página original: {page_number}")
print(chunk_data)
print(page_chunks_with_metadata)