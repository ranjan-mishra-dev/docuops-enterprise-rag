from pathlib import Path

from app.rag.loader import load_pdf


def ingest_document(file_path: str | Path):
    """
    Run the document ingestion pipeline.
    """

    documents = load_pdf(file_path)

    return documents