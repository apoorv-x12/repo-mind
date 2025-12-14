# pylint: disable=import-error
# backend/embeddings.py
from chromadb import Client

client = Client()
collection = client.create_collection("repo")

def add_chunks(chunks):
    collection.add(
        documents=[c["content"] for c in chunks],
        metadatas=[{"file": c["file"]} for c in chunks],
        ids=[str(i) for i in range(len(chunks))]
    )
