from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.pipelines.rag_pipeline import answer_question

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = answer_question(request.question)
        return result

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate answer.",
        )

