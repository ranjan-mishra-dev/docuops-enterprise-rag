import logging

from fastapi import FastAPI
from app.config import settings
from app.logging_config import setup_logging

from app.api.routes.documents import router as documents_router
setup_logging()

logger = logging.getLogger(__name__)
app = FastAPI(title=settings.app_name)

app.include_router(documents_router, prefix="/api")



@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "message": "DocuOps API is running",
        "environment": settings.environment,
    }