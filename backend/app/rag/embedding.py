from langchain_core.documents import Document
from langchain_mistralai import MistralAIEmbeddings

from app.config import settings


def get_embedding_model() -> MistralAIEmbeddings:
    """
    Initialize the Mistral embedding model.
    """

    if not settings.mistral_api_key:
        raise ValueError("MISTRAL_API_KEY is missing from .env")

    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        mistral_api_key=settings.mistral_api_key,
    )

    return embeddings


def embed_documents(
    chunks: list[Document],
) -> list[list[float]]:
    """
    Convert document chunks into embedding vectors.
    """

    embeddings = get_embedding_model()

    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors

# this embedding we using to keep the check whether embedding model working or not, embedding work we are doing in vector_Store.py