from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "DocuOps"
    environment: str = "development"
    log_level: str = "INFO"
    
    gemini_api_key: str = "AQ.Ab8RN6IJuLFCqhAafULmkoywdqQP-oTw-UNBEgidNQ1kXaYKjA"

    chroma_path: str = "./data/chroma"
    documents_path: str = "./data/documents"

    class Config:
        env_file = ".env"


settings = Settings()