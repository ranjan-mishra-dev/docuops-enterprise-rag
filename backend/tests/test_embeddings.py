# from app.rag.embeddings import get_embedding_model
from app.rag.embedding import embed_documents
from app.pipelines.ingestion_pipeline import ingest_document

PDF_PATH = "data/documents/hr_document.pdf"

def main():
    chunks = ingest_document(PDF_PATH)

    print("Total chunks:", len(chunks))

    vectors = embed_documents(chunks)
    print("Total vectors:", len(vectors))

    if vectors:
        print("Vector dimensions:", len(vectors[0]))
        print("First 5 values:", vectors[0][:5])


if __name__ == "__main__":
    main()