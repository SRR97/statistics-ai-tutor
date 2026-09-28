import json
from pathlib import Path
from app.rag import initialize_rag
from app.retriever import retrieve_relevant_chunks

TEST_CASES_PATH = Path(__file__).parent / "retrieval_test_cases.json"

def load_test_cases():
    with open(TEST_CASES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    test_cases = load_test_cases()
    chunks, chunk_embeddings = initialize_rag()
    test_case = test_cases[0]
    query = test_case["query"]
    expected_sources = test_case["expected_sources"]

    results = retrieve_relevant_chunks(
        query,
        chunks,
        chunk_embeddings,
        top_k=3
    )

    hit_at_3 = False
    first_relevant_rank = None

    for rank, result in enumerate(results, start=1):
        chunk = result["chunk"]

        retrieved_source = {
            "document": chunk["document"],
            "page": chunk["page_number"]
        }

        is_expected = retrieved_source in expected_sources

        if is_expected:
            hit_at_3 = True

            if first_relevant_rank is None:
                first_relevant_rank = rank

        print(
            chunk["document"],
            "- página",
            chunk["page_number"],
            "- similitud:",
            round(result["similarity"], 4)
        )

    if first_relevant_rank is not None:
        reciprocal_rank = 1 / first_relevant_rank
    else:
        reciprocal_rank = 0    

    hit_at_1 = first_relevant_rank == 1    

    print("Hit@1:", hit_at_1)
    print("Hit@3:", hit_at_3)
    print("First relevant rank:", first_relevant_rank)
    print("Reciprocal rank:", reciprocal_rank)