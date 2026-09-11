from retriever import retrieve_relevant_chunks
from document_loader import load_pdf
from text_splitter import chunk_pages
from embeddings import create_embeddings
from openai import OpenAI

client = OpenAI()

def generate_rag_answer(query, chunks, chunk_embeddings):

    relevant_chunks = retrieve_relevant_chunks(
        query,
        chunks,
        chunk_embeddings,
        top_k=3
    )

    if not relevant_chunks:
        return "No hay información suficiente en los apuntes proporcionados para responder la pregunta."
    
    context_parts = []

    for result in relevant_chunks:

        chunk = result["chunk"]
        page_number = chunk["page_number"]
        text = chunk["text"]
        context_part = f"Página {page_number}:\n{text}"
        context_parts.append(context_part)
        
    context = "\n\n".join(context_parts)
    system_prompt = "Eres un tutor académico de Estadística. Responde utilizando únicamente la información proporcionada en el contexto."
    system_prompt += " Si el contexto no contiene información suficiente para responder la pregunta, indica claramente que no hay información suficiente en los apuntes proporcionados."
    system_prompt += " Indica siempre la página o páginas del contexto utilizadas para elaborar la respuesta."

    user_prompt = f"Contexto:\n{context}\n\nPregunta:\n{query}"

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=system_prompt,
        input=user_prompt
    )

    return response.output_text

if __name__ == "__main__":
    pages = load_pdf("data/Clase_2_Análisis_de_regresión.pdf")
    chunks = chunk_pages(pages, chunk_size=500, overlap=100)

    chunk_texts = [chunk["text"] for chunk in chunks]
    chunk_embeddings = create_embeddings(chunk_texts)

    test_query = "¿Cómo se interpreta el coeficiente beta uno?"
    answer = generate_rag_answer(test_query, chunks, chunk_embeddings)

    print(answer)