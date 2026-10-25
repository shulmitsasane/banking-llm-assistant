from document_loader import load_documents


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks


def create_chunks():
    documents = load_documents()

    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["content"])

        for index, chunk in enumerate(chunks):
            all_chunks.append({
                "source": document["source"],
                "chunk_id": index,
                "content": chunk
            })

    return all_chunks


if __name__ == "__main__":
    chunks = create_chunks()

    print("Total chunks created:", len(chunks))

    for chunk in chunks[:5]:
        print("\nSOURCE:", chunk["source"])
        print("CHUNK ID:", chunk["chunk_id"])
        print(chunk["content"])
        print("-" * 50)