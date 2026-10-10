# we were getting everything from retriever in form of document but we only need few things thats why took some part that will pass to llm

from langchain_core.documents import Document


def build_context(documents: list[Document]) -> str:
    """Combine retrieved documents into a formatted context."""

    if not documents:
        return "No relevant documents found."

    context_parts = []

    for i, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", "Unknown page")

        # PyPDFLoader uses zero-based page numbers
        if isinstance(page, int):
            page = page + 1

        section = (
            f"[Source {i}]\n"
            f"File: {source}\n"
            f"Page: {page}\n"
            f"Content:\n{doc.page_content}"
        )

        context_parts.append(section)

    return "\n\n".join(context_parts)