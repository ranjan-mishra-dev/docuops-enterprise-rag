from pathlib import Path
from fastapi import UploadFile
from app.config import settings
from app.pipelines.ingestion_pipeline import ingest_document



class DocumentService:

    def __init__(self):
        self.documents_path = Path(settings.documents_path)
        self.documents_path.mkdir(parents=True, exist_ok=True)

    async def save_document(self, file: UploadFile) -> dict:
        file_path = self.documents_path / file.filename

        contents = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(contents)

        documents = ingest_document(file_path)


        return {
            "filename": file.filename,
            "path": str(file_path),
            "size": len(contents),
            "chunks": len(documents)
        }