from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings
from langchain_core.prompts import ChatPromptTemplate


def get_llm():
    """Initialize the LLM."""

    if not settings.gemini_api_key:
        raise ValueError("GEMINI_API_KEY is missing")

    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        api_key=settings.gemini_api_key,
        temperature=0,
    )


def generate_answer(query: str, context: str) -> str:
    """Generate an answer using retrieved context."""

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are DocuOps, an AI assistant that answers
            questions using the provided document context.

            Rules:
            1. Answer only using the provided context.
            2. Do not invent facts or use outside knowledge.
            3. If the context does not contain the answer,
               clearly say that the information is not
               available in the provided documents.
            4. Keep the answer clear and concise.
            5. Mention relevant source and page information
               when available.
            """
        ),
        (
            "human",
            """
            Document Context:
            {context}

            User Question:
            {question}

            Answer:
            """
        )
    ])

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": query,
    })

    return response.content[0]['text']