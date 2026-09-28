from pathlib import Path

from app.rag.loader import load_pdf
from app.rag.cleaner import clean_documents
from app.rag.chunker import chunk_documents


def ingest_document(file_path: str | Path):
    """
    Run the document ingestion pipeline.
    """

    documents = load_pdf(file_path)
    # print("document size: ", len(documents))
    cleaned_documents = clean_documents(documents)
    chunks = chunk_documents(cleaned_documents)
    # print("chunk size: ", len(chunks))
    return chunks
    # return documents