# backend/app.py
from fastapi import FastAPI
from ingest import clone_repo, collect_files
from chunker import chunk_code
from embeddings import add_chunks
from retrieval import retrieve
from llm import ask_llm
from impact import find_impacted

app = FastAPI()

@app.post("/ingest")
def ingest_repo(url: str):
    repo = clone_repo(url)
    files = collect_files(repo)

    chunks = []
    for f in files:
        code = f.read_text(errors="ignore")
        for c in chunk_code(code):
            chunks.append({"file": str(f), "content": c})

    add_chunks(chunks)
    return {"files_indexed": len(files)}

@app.post("/ask")
def ask(q: str):
    chunks = retrieve(q)
    context = "\n".join(c["content"] for c in chunks)
    answer = ask_llm(context, q)
    return {
        "answer": answer,
        "sources": list(set(c["file"] for c in chunks))
    }
