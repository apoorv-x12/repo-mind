# pylint: disable=import-error
# backend/retrieval.py
from embeddings import collection

def retrieve(query, k=5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )
    return [
        {
            "content": doc,
            "file": meta["file"]
        }
        for doc, meta in zip(
            results["documents"][0],
            results["metadatas"][0]
        )
    ]
