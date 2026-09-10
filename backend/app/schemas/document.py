from pydantic import BaseModel


class DocumentInfo(BaseModel):
    filename: str
    path: str
    size: int
    pages: int


class DocumentUploadResponse(BaseModel):
    message: str
    document: DocumentInfo