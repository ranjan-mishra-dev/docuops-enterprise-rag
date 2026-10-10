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

def document_exist(document_id: str) -> bool:
    '''using to check whether this chunk already exist or not if yes then update with newone'''

    vector_store = get_vector_store()
    result = vector_store.get(
        where={"document_id":document_id},
        limit=1
    )

    return bool(result['ids'])

    



def add_chunks(chunks: list[Document], document_id: str) -> int:
    """Embed and store document chunks in ChromaDB."""
    # print("8.0")


    if not chunks:
        return 0

    # print("8")

    vector_store = get_vector_store()
    ids = []

    for index, chunk in enumerate(chunks):
        chunk.metadata["document_id"] = document_id
        ids.append(f"{document_id}:{index}")
    
    # print("9")

    # Stable IDs prevent duplicate records on repeated uploads.
    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )

    '''
    what this add_chunks doing: ChromaDB, through LangChain, Takes the text from each chunk, Sends it to the Mistral embedding model.
    Receives a vector for each chunk, Stores the vector, original text, and metadata in the collection.
    '''

    return len(chunks)



def delete_document(document_id: str) -> int:
    """Delete all indexed chunks belonging to a document."""

    store = get_vector_store()

    result = store.get(
        where={"document_id": document_id},
    )

    ids = result["ids"]

    if ids:
        store.delete(ids=ids)

    return len(ids)