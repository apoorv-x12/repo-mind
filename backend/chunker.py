# backend/chunker.py
def chunk_code(code, max_chars=1500):
    blocks = code.split("\n\n")
    chunks = []

    for b in blocks:
        if len(b.split()) < 30:
            continue
        chunks.append(b[:max_chars])

    return chunks
