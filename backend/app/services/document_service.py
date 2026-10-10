from pathlib import Path
from fastapi import UploadFile
from app.config import settings
from app.pipelines.ingestion_pipeline import ingest_document
from app.rag.vector_store import add_chunks, document_exist
import hashlib


class DocumentService:

    def __init__(self):
        self.documents_path = Path(settings.documents_path)
        self.documents_path.mkdir(parents=True, exist_ok=True)

    async def save_document(self, file: UploadFile) -> str:
        file_path = self.documents_path / file.filename

        contents = await file.read()

        print("2")


        with open(file_path, "wb") as buffer:
            buffer.write(contents)

        print("3")


        return file_path



def process_document(file_path: Path) -> int:
    """Ingest a document and store its chunks in ChromaDB."""

    # print("5")

    document_id = hashlib.sha256(file_path.read_bytes()).hexdigest()

    if document_exist(document_id):
        return {
            "document_id": document_id,
            "chunks": 0,
            "status": "already_indexed"
        }

    
    # print("6")

    chunks = ingest_document(file_path)
    # print("7")
    # print("chunks", chunks)
    # print("document_id", document_id)

    count = add_chunks(chunks, document_id)
    # print("7.1")


    return {"document_id": document_id,
            "chunks": count,
            "status": "indexed"
            }