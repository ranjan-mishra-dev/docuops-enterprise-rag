import logging
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from app.config import settings
from app.logging_config import setup_logging

from app.api.routes.documents import router as documents_router
from app.api.routes import documents, chat

setup_logging()

logger = logging.getLogger(__name__)
app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents_router, prefix="/api")
app.include_router(chat.router)

@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "message": "DocuOps API is running",
        "environment": settings.environment,
    }