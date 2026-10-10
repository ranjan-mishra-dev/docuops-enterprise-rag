from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    source: str
    page: int | None = None
    content: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]