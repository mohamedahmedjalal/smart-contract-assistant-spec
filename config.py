import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

UPLOAD_DIR = "data/uploads"
CHROMA_DIR = "data/chroma_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

MODEL_NAME = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
