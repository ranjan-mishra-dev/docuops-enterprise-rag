from app.services.document_service import (DocumentService, process_document)
from fastapi import APIRouter, UploadFile, File, HTTPException
router = APIRouter(prefix="/documents", tags=["Documents"])

from app.schemas.document import DocumentUploadResponse
document_service = DocumentService()

from pathlib import Path
from app.config import settings
from app.rag.vector_store import delete_document
from app.services.document_registry import (
    get_all_documents,
    get_document,
    remove_document_record
)

# /api/documents: GET
@router.get("")
def list_documents():
    return {
        "documents": get_all_documents()
    }

# /api/documents/{id}: Delete by id
@router.delete("/{document_id}")
def remove_document(document_id: str):
    record = get_document(document_id=document_id)
    if record is None:
        raise HTTPException(
            status_code=404,
            detail= "document not found.",
        )

    delete_document(document_id)
    document_str = Path(settings.documents_path).resolve()
    file_path = Path(record["file_path"]).resolve()

    if file_path.parent == document_str and file_path.is_file():
        file_path.unlink()

    remove_document_record(document_id)
    return {
        "message": "document deleted successfully",
        "document_id": document_id
    }



# /api/documents/upload: POST
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



    