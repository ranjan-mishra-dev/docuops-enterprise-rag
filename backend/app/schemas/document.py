from pydantic import BaseModel


class DocumentInfo(BaseModel):
    filename: str
    path: str
    size: int
    chunks: int


class DocumentUploadResponse(BaseModel):
    message: str
    document: DocumentInfo