# from app.rag.loader import load_pdf
from app.rag.loader import load_pdf


PDF_PATH = "data/documents/hr_document.pdf"


def main():
    documents = load_pdf(PDF_PATH)

    print(f"Pages loaded: {len(documents)}")

    for i, document in enumerate(documents):
        print(f"\n--- Page {i + 1} ---")
        print(document.page_content[:500])
        print("Metadata:", document.metadata)


if __name__ == "__main__":
    main()