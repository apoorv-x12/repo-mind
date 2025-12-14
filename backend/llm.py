# pylint: disable=import-error
# backend/llm.py
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(context, question):
    prompt = f"""
Answer ONLY using the context below.
If insufficient, say: Not enough context.

Context:
{context}

Question:
{question}
"""
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return resp.choices[0].message.content
