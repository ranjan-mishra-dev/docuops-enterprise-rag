from app.rag.retriever import retrieve_chunks
from app.rag.context_builder import build_context
from app.rag.generator import generate_answer


def answer_question(query: str) -> dict:
    """Run the complete RAG pipeline."""

    if not query.strip():
        raise ValueError("Question cannot be empty")

    # Step 1: Retrieve relevant chunks
    chunks = retrieve_chunks(query, k=4)
    print("chunks: ", chunks)

    # Step 2: Build context
    context = build_context(chunks)

    # Step 3: Generate answer
    answer = generate_answer(query, context)

    # Step 4: Return answer and source information
    sources = []

    for chunk in chunks:
        sources.append({
            "source": chunk.metadata.get("source", "Unknown"),
            "page": (
                chunk.metadata.get("page", 0) + 1
                if isinstance(chunk.metadata.get("page"), int)
                else None
            ),
            "content": chunk.page_content,
        })

    return {
        "question": query,
        "answer": answer,
        "sources": sources,
    }