from embeddings import create_embedding, create_embeddings
from similarity import cosine_similarity
from document_loader import load_pdf
from text_splitter import chunk_pages

def retrieve_relevant_chunks(query, chunks, chunk_embeddings, top_k=3, similarity_threshold=0.40):
    query_embedding = create_embedding(query)

    
    results = []

    for chunk, chunk_embedding in zip(chunks, chunk_embeddings):
        similarity = cosine_similarity(query_embedding, chunk_embedding)

        result = {
            "chunk": chunk,
            "similarity": similarity
        }

        if similarity >= similarity_threshold:
            results.append(result)

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]

if __name__ == "__main__":
    pages = load_pdf("data/Clase_2_Análisis_de_regresión.pdf")
    chunks = chunk_pages(pages, chunk_size=500, overlap=100)

    chunk_texts = [chunk["text"] for chunk in chunks]
    chunk_embeddings = create_embeddings(chunk_texts)

    test_query = "¿Qué es una red neuronal convolucional?"
    test_results = retrieve_relevant_chunks(test_query, chunks, chunk_embeddings, top_k=3)

    print(test_results)
          
    