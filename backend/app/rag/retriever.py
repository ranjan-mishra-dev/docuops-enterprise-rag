from langchain_core.documents import Document

from app.rag.vector_store import get_vector_store


def retrieve_chunks(
    query: str,
    k: int = 4,
) -> list[Document]:
    """Retrieve the most relevant chunks for a user query."""

    if not query.strip():
        raise ValueError("Query cannot be empty")

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query=query,
        k=k,
    )

    return results
# return documents