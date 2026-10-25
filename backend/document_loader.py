from pathlib import Path

DOCUMENTS_FOLDER = Path("documents")

def load_documents():
    documents = []

    for file_path in DOCUMENTS_FOLDER.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents


if __name__ == "__main__":
    docs = load_documents()

    for doc in docs:
        print("SOURCE:", doc["source"])
        print(doc["content"])
        print("-" * 50)