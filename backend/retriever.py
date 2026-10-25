import numpy as np
from embeddings import create_embeddings, get_embedding


# Create document embeddings only once when the backend starts
CHUNKS, EMBEDDINGS = create_embeddings()


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


def retrieve_relevant_chunks(question, top_k=3, min_score=0.45):
    # Create an embedding for the user's question
    question_embedding = get_embedding(question)

    scored_chunks = []

    # Compare the question embedding with every document chunk embedding
    for chunk, embedding in zip(CHUNKS, EMBEDDINGS):
        score = cosine_similarity(
            question_embedding,
            embedding
        )

        scored_chunks.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "content": chunk["content"],
            "score": float(score)
        })

    # Sort chunks from highest similarity to lowest similarity
    scored_chunks.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # Keep only chunks that are relevant enough
    relevant_chunks = [
        chunk
        for chunk in scored_chunks
        if chunk["score"] >= min_score
    ]

    # Return only the top relevant chunks
    return relevant_chunks[:top_k]


if __name__ == "__main__":
    question = "Who won the Cricket World Cup?"

    results = retrieve_relevant_chunks(question)

    print("QUESTION:", question)

    if not results:
        print("\nNo sufficiently relevant chunks were found.")

    for result in results:
        print("\nSOURCE:", result["source"])
        print("CHUNK ID:", result["chunk_id"])
        print("SIMILARITY SCORE:", result["score"])
        print(result["content"])
        print("-" * 50)