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

        # print("1")
        file_path = await document_service.save_document(file)
        # print("4")

        result = process_document(file_path)

        message = (
            "Document indexed successfully."
            if result["status"] == "indexed"
            else "This document already indexed."
        )

        return {
            "filename": file.filename,
            "message": message,
            "chunks": result["chunks"],
        }


    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
        status_code=500,
        detail="Failed to process document.",
        )