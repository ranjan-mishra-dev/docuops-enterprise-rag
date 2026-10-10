from pydantic import BaseModel


# class DocumentInfo(BaseModel):
#     filename: str
#     path: str
#     size: int
#     chunks: int


class DocumentUploadResponse(BaseModel):
    filename: str
    message: str
    chunks: int