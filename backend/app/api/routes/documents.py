from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.config import settings
router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    documents_path = Path(settings.documents_path)
    documents_path.mkdir(parents=True, exist_ok=True)

    file_path = documents_path / file.filename

    contents = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "path": str(file_path),
    }