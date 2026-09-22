from app.retriever import retrieve_relevant_chunks
from app.document_loader import load_pdfs_from_directory
from app.text_splitter import chunk_pages
from app.embeddings import create_embeddings
from openai import OpenAI

client = OpenAI()

def initialize_rag():
    pages = load_pdfs_from_directory("data")
    chunks = chunk_pages(pages, chunk_size=500, overlap=100)

    chunk_texts = [chunk["text"] for chunk in chunks]
    chunk_embeddings = create_embeddings(chunk_texts)

    return chunks, chunk_embeddings

def generate_rag_answer(query, chunks, chunk_embeddings):

    relevant_chunks = retrieve_relevant_chunks(
        query,
        chunks,
        chunk_embeddings,
        top_k=3
    )

    if not relevant_chunks:
        return {
            "answer": "No hay información suficiente en los apuntes proporcionados para responder la pregunta.",
            "sources": []
        }

    context_parts = []
    sources = []

    for result in relevant_chunks:

        chunk = result["chunk"]
        document_name = chunk["document"]
        page_number = chunk["page_number"]

        source = {
            "document": document_name,
            "page": page_number
        }

        if source not in sources:
            sources.append(source)

            text = chunk["text"]
            context_part = f"Documento: {document_name}, página {page_number}:\n{text}"
            context_parts.append(context_part)
        
    context = "\n\n".join(context_parts)
    system_prompt = "Eres un tutor académico de Estadística. Responde utilizando únicamente la información proporcionada en el contexto."
    system_prompt += " Si el contexto no contiene información suficiente para responder la pregunta, indica claramente que no hay información suficiente en los apuntes proporcionados."
    system_prompt += " Para escribir expresiones matemáticas en LaTeX, usa $...$ para expresiones en línea y $$...$$ para expresiones en bloque. No uses \\(...\\) ni \\[...\\]."
    
    user_prompt = f"Contexto:\n{context}\n\nPregunta:\n{query}"

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=system_prompt,
        input=user_prompt
    )

    return {
        "answer": response.output_text,
        "sources": sources
    }

if __name__ == "__main__":
    
    chunks, chunk_embeddings = initialize_rag()

    while True:
        query = input("Tu pregunta: ")

        if query.lower() == "salir":
            break

        answer = generate_rag_answer(query, chunks, chunk_embeddings)
        print(answer)