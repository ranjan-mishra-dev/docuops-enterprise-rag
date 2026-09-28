from app.pipelines.ingestion_pipeline import ingest_document


PDF_PATH = "data/documents/hr_document.pdf"


def main():
    chunks = ingest_document(PDF_PATH)

    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:5]):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk.page_content)
        print(f"\nLength: {len(chunk.page_content)}")
        print(f"Metadata: {chunk.metadata}")


if __name__ == "__main__":
    main()