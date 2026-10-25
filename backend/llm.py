import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"


def generate_answer(question, context):
    prompt = f"""
You are a banking support assistant.

Answer the user's question using only the context provided below.

If the answer is not available in the context, say:
"I do not have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]


if __name__ == "__main__":
    test_context = """
FT102 means that the customer has insufficient available balance.
Before retrying, the customer should check the available balance.
"""

    answer = generate_answer(
        "Why did my fund transfer fail because I don't have enough money?",
        test_context
    )

    print(answer)