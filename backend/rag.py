from retriever import retrieve_relevant_chunks
from llm import generate_answer


def answer_question(question):
    relevant_chunks = retrieve_relevant_chunks(question, top_k=3)

    if not relevant_chunks:
        return {
            "question": question,
            "answer": "I do not have enough information in the provided documents.",
            "sources": []
        }

    context_parts = []

    for chunk in relevant_chunks:
        context_parts.append(
            f"Source: {chunk['source']}\n"
            f"{chunk['content']}"
        )

    context = "\n\n".join(context_parts)

    answer = generate_answer(question, context)

    sources = list({
        chunk["source"]
        for chunk in relevant_chunks
    })

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    question = "Why did my fund transfer fail because I do not have enough balance?"

    result = answer_question(question)

    print("\nQUESTION:")
    print(result["question"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")
    print(result["sources"])