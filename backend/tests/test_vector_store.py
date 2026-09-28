from app.pipelines.ingestion_pipeline import ingest_document
from app.rag.vector_store import add_chunks, get_vector_store


def test_vector_store():
    # Step 1: Load, clean, and chunk the PDF
    chunks = ingest_document("data/documents/hr_document.pdf")

    # Step 2: Store chunks in ChromaDB
    count = add_chunks(chunks)

    print(f"Stored {count} chunks in ChromaDB")

    # Step 3: Check stored collection
    vector_store = get_vector_store()

    print("Total records:", vector_store._collection.count())


if __name__ == "__main__":
    test_vector_store()