from pathlib import Path
from fastapi import UploadFile
from app.config import settings
from app.pipelines.ingestion_pipeline import ingest_document
from app.rag.vector_store import add_chunks


class DocumentService:

    def __init__(self):
        self.documents_path = Path(settings.documents_path)
        self.documents_path.mkdir(parents=True, exist_ok=True)

    async def save_document(self, file: UploadFile) -> str:
        file_path = self.documents_path / file.filename

        contents = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(contents)

    # get chunks of pdf u uploaded
        documents = ingest_document(file_path)


        return file_path



def process_document(file_path: Path) -> int:
    """Ingest a document and store its chunks in ChromaDB."""

    chunks = ingest_document(file_path)

    stored_chunks = add_chunks(chunks)

    return stored_chunks