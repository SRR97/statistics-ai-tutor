from retriever import retrieve_relevant_chunks
from openai import OpenAI

client = OpenAI()

def generate_rag_answer(query, chunks):

    relevant_chunks = retrieve_relevant_chunks(query, chunks, top_k=3)
    context_parts = []

    for result in relevant_chunks:

        chunk = result["chunk"]
        page_number = chunk["page_number"]
        text = chunk["text"]
        context_part = f"Página {page_number}:\n{text}"
        context_parts.append(context_part)