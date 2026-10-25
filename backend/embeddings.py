import requests
from chunker import create_chunks

OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "nomic-embed-text"


def get_embedding(text):
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": EMBED_MODEL,
            "input": text
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"][0]


def create_embeddings():
    chunks = create_chunks()

    embeddings = []

    for chunk in chunks:
        embedding = get_embedding(chunk["content"])
        embeddings.append(embedding)

    return chunks, embeddings


if __name__ == "__main__":
    chunks, embeddings = create_embeddings()

    print("Number of chunks:", len(chunks))
    print("Number of embeddings:", len(embeddings))

    print("\nFirst chunk:")
    print(chunks[0]["content"])

    print("\nFirst embedding:")
    print(embeddings[0][:10])

    print("\nEmbedding dimensions:")
    print(len(embeddings[0]))