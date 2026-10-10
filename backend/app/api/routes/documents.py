from app.services.document_service import (DocumentService, process_document)
from fastapi import APIRouter, UploadFile, File, HTTPException
router = APIRouter(prefix="/documents", tags=["Documents"])

from app.schemas.document import DocumentUploadResponse
document_service = DocumentService()



@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):

    try:
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename is missing.",
            )

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported.",
            )

        file_path = await document_service.save_document(file)
        chunks_count = process_document(file_path)

        return {
            "filename": file.filename,
            "message": "Document uploaded and indexed successfully.",
            "chunks": chunks_count,
        }


    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
        status_code=500,
        detail="Failed to process document.",
        )