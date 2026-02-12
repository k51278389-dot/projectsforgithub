# PDF Question Answering using Retrieval-Augmented Generation (RAG)

## Overview
This project implements a **retrieval-augmented generation (RAG)** pipeline for answering questions over PDF documents.
The system retrieves semantically relevant document chunks using embeddings and only then uses a language model to generate grounded answers.

The focus of this project is **retrieval correctness, transparency, and engineering clarity**, rather than UI or framework abstractions.

---

## Key Concepts Covered
- Retrieval-Augmented Generation (RAG)
- SentenceTransformer embeddings
- Semantic similarity search (cosine similarity)
- Sentence-based chunking with overlap
- Metadata preservation (page number, chunk ID)
- Grounded prompt construction
- Local LLM inference via Ollama

---

## Pipeline Overview
1. Load and parse PDF documents
2. Clean and normalize extracted text
3. Split text into sentences
4. Build overlapping text chunks
5. Generate embeddings using SentenceTransformers
6. Perform semantic retrieval using cosine similarity
7. Construct a strictly grounded prompt
8. Generate an answer using a local LLM (optional)

Retrieval quality is validated independently of generation.

---

## Project Structure
```text
genai_git/
│
├── genai_rag.py
├── data/
│   └── object_oriented_python_tutorial.pdf
├── README.md
└── requirements.txt
