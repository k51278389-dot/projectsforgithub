# ============================================================
# 1. Imports & Configuration
# ============================================================
from pypdf import PdfReader
import numpy as np
import requests
import re
from sentence_transformers import SentenceTransformer


PDF_PATH = r"d:\pdfmatforgenai\object_oriented_python_tutorial.pdf"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3:mini"


# ============================================================
# 2. Load & Read PDF
# ============================================================
reader = PdfReader(PDF_PATH)

pages = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        pages.append({
            "page": i + 1,
            "text": text
        })

print(f"Loaded {len(pages)} pages from PDF")


# ============================================================
# 3. Text Cleaning & Normalization
# ============================================================
def clean_text(text: str) -> str:
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        clean_lines.append(line)

    return "\n".join(clean_lines)


def normalize_text(text: str) -> str:
    text = text.replace("•", ". ")
    text = text.replace("–", ". ")
    text = text.replace("-", ". ")
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


# ============================================================
# 4. Chunking Strategy (Sentence-based with overlap)
# ============================================================
def build_chunks(sentences, max_chars=600, overlap_sentences=1):
    chunks = []
    current = []

    for sentence in sentences:
        current.append(sentence)

        if len(" ".join(current)) >= max_chars:
            chunks.append(" ".join(current))
            current = current[-overlap_sentences:]

    if current:
        chunks.append(" ".join(current))

    return chunks


chunks = []

for page in pages:
    cleaned = clean_text(page["text"])
    normalized = normalize_text(cleaned)
    sentences = split_sentences(normalized)
    page_chunks = build_chunks(sentences)

    for i, chunk in enumerate(page_chunks):
        chunks.append({
            "text": chunk,
            "page": page["page"],
            "chunk_id": i
        })

print(f"Built {len(chunks)} chunks")


# ============================================================
# 5. Embedding Model
# ============================================================
embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def embed_text(text: str) -> np.ndarray:
    return embed_model.encode(
        text,
        normalize_embeddings=True
    )


embeddings = []
valid_chunks = []

for chunk in chunks:
    if not chunk["text"].strip():
        continue

    embeddings.append(embed_text(chunk["text"]))
    valid_chunks.append(chunk)

chunks = valid_chunks

print(f"Embedded {len(embeddings)} chunks")


# ============================================================
# 6. Similarity Function (Cosine)
# ============================================================
def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ============================================================
# 7. Retrieval (Top-K Semantic Search)
# ============================================================
def retrieve_top_chunks(question, chunks, embeddings, top_k=2):
    question_embedding = embed_text(question)

    scores = []
    for i, emb in enumerate(embeddings):
        score = cosine_similarity(question_embedding, emb)
        scores.append((i, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    top = scores[:top_k]

    return [(chunks[i], score) for i, score in top]


# ============================================================
# 8. Prompt Construction (Strict Grounding)
# ============================================================
def build_prompt(question, retrieved_chunks):
    context = ""
    for chunk, _ in retrieved_chunks:
        context += f"[Page {chunk['page']}] {chunk['text']}\n\n"

    return f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""


# ============================================================
# 9. Local LLM Interface (Ollama)
# ============================================================
def ask_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    if "response" in data:
        return data["response"]

    if "error" in data:
        raise RuntimeError(f"Ollama error: {data['error']}")

    raise RuntimeError(f"Unexpected Ollama response format: {data}")


# ============================================================
# 10. End-to-End RAG Execution
# ============================================================
question = "What is inheritance in OOP and why is it used?"

retrieved = retrieve_top_chunks(
    question=question,
    chunks=chunks,
    embeddings=embeddings,
    top_k=2
)

print("\n=== RETRIEVED CHUNKS ===")
for chunk, score in retrieved:
    print(f"\n[SCORE: {score:.4f}] Page {chunk['page']}")
    print(chunk["text"])

prompt = build_prompt(question, retrieved)

# Uncomment when LLM is available
answer = ask_llm(prompt)
print("\n=== ANSWER ===\n")
print(answer)
