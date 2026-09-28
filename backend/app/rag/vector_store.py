from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import settings
from app.rag.embedding import get_embedding_model


COLLECTION_NAME = "docuops_documents"


def get_vector_store() -> Chroma:
    """Create or connect to the persistent ChromaDB collection."""

    persist_directory = Path(settings.chroma_path)
    persist_directory.mkdir(parents=True, exist_ok=True)

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=str(persist_directory),
    )

    return vector_store


def add_chunks(chunks: list[Document]) -> int:
    """Embed and store document chunks in ChromaDB."""

    if not chunks:
        return 0

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)
    '''
    what this add document doing: ChromaDB, through LangChain, Takes the text from each chunk, Sends it to the Mistral embedding model.
    Receives a vector for each chunk, Stores the vector, original text, and metadata in the collection.
    '''

    return len(chunks)