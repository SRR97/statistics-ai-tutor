def chunk_text(text, chunk_size, overlap):

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

def chunk_pages(pages, chunk_size, overlap):
    document_chunks = []

    for page in pages:
        page_text = page["text"]
        page_number = page["page_number"]
        page_chunks = chunk_text(page_text, chunk_size, overlap)

        for chunk_number, chunk in enumerate(page_chunks, start=1):
            chunk_data = {
                "page_number": page_number,
                "chunk_number": chunk_number,
                "text": chunk
            }
            document_chunks.append(chunk_data)
    return document_chunks

