from fastapi import FastAPI, UploadFile, File
import os

from app.utils import extract_text
from app.ingestion import chunk_document
from app.embeddings import store_embeddings
from app.qa_chain import ask_question
from app.summarizer import summarize_contract
from app.config import UPLOAD_DIR

app = FastAPI(title="Smart Contract Assistant")


@app.get("/")
def home():
    return {"message": "Smart Contract Assistant API Running"}


@app.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)

    chunks = chunk_document(text)

    store_embeddings(chunks)

    summary = summarize_contract(text[:12000])

    return {
        "message": "File processed successfully",
        "chunks": len(chunks),
        "summary": summary,
    }


@app.post("/ask")
def ask(data: dict):
    question = data["question"]
    answer = ask_question(question)

    return {
        "answer": answer
    }
