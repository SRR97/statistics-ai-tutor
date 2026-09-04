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