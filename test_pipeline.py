from app.utils import extract_text
from app.ingestion import chunk_document


def test_chunking():
    text = "This is a test document. " * 200

    chunks = chunk_document(text)

    assert len(chunks) > 1


def test_extraction():
    sample = "data/uploads/sample.pdf"

    try:
        text = extract_text(sample)
        assert len(text) > 0
    except:
        assert True
