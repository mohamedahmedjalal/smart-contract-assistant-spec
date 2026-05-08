from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import CHROMA_DIR

# This uses a free model that runs on your CPU
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def store_embeddings(chunks):
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return vectorstore

def load_vectorstore():
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )