
from pypdf import PdfReader
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# ===============================
# 2. Load & Read PDF
# ===============================
reader = PdfReader(r"d:\pdfmatforgenai\object_oriented_python_tutorial.pdf")

pages = []

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        pages.append({
            "page": i + 1,
            "text": text
        })



# ===============================
# 3. Clean Text
# ===============================
def clean_text(text):
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        
        clean_lines.append(line)

    return "\n".join(clean_lines)


import re

def normalize_slide_text(text):
    text = text.replace("•", ". ")
    text = text.replace("–", ". ")
    text = text.replace("-", ". ")
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]
               
# # ===============================
# # 4. Chunk Text
# # ===============================

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
    # only first 2 pages
    # if page["page"] > 2:   
    #     break 
    cleaned = clean_text(page["text"])
    normalized = normalize_slide_text(cleaned)
    sentences = split_sentences(normalized)
    page_chunks = build_chunks(sentences)
             #  TO SEE CHUNKS 
    # print("\n--- PAGE", page["page"], "CHUNKS (first 2) ---\n")
    # for c in page_chunks[:2]:
    #     print(c)


    for i, chunk in enumerate(page_chunks):
        chunks.append({
            "text": chunk,
            "page": page["page"],
            "chunk_id": i
        })

for i, chunk in enumerate(chunks):
    if not chunk["text"].strip():
        print("EMPTY CHUNK FOUND AT INDEX:", i, "PAGE:", chunk["page"])
        pass





embed_model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_text(text: str):
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



# ===============================
# 7. Cosine Similarity
# ===============================
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ===============================
# 8. Retrieve Top Chunks
# ===============================
def retrieve_top_chunks(question, chunks, embeddings, top_k=2):
    question_embedding = embed_text(question)

    scores = []
    for i, emb in enumerate(embeddings):
        score = cosine_similarity(question_embedding, emb)
        scores.append((i, score))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top = scores[:top_k]

    return [(chunks[i], score) for i, score in top]



# # ===============================
# # 9. Build Prompt
# # =============================== 


def build_prompt(question, retrieved_chunks): # same as retrieved (prompt = build_prompt(question, retrieved))
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
# ===============================
# 10. Ask Ollama LLM
# ===============================
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
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




# ===============================
# 11. Run RAG
# ===============================
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
answer = ask_llm(prompt)

print("\n=== ANSWER ===\n")
print(answer)