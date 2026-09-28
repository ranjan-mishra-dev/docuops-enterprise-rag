from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    app_name: str = "DocuOps"
    environment: str = "development"
    log_level: str = "INFO"
    
    gemini_api_key: str = ""
    mistral_api_key: str = ""

    chroma_path: str = str(BASE_DIR / "data" / "chroma")
    documents_path: str = str(BASE_DIR / "data" / "documents")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()