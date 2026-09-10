from app.services.document_service import DocumentService
from fastapi import APIRouter, UploadFile, File, HTTPException
router = APIRouter(prefix="/documents", tags=["Documents"])

from app.schemas.document import DocumentUploadResponse
document_service = DocumentService()



@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    document = await document_service.save_document(file)

    return {
        "message": "Document uploaded successfully",
        "document": document
    }