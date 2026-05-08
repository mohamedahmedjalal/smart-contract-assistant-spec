import os
import fitz
import pdfplumber
from docx import Document


def extract_pdf_text(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()

    return text


def extract_docx_text(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_pdf_text(file_path)

    elif ext == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")
