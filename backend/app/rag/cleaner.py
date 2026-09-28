import re

from langchain_core.documents import Document


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text while preserving meaningful content.
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing spaces from each line
    text = "\n".join(line.strip() for line in text.split("\n"))

    # Replace 3+ consecutive newlines with 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def clean_documents(documents: list[Document]) -> list[Document]:
    """
    Clean the text content of all loaded documents.
    """

    for document in documents:
        document.page_content = clean_text(document.page_content)

    return documents