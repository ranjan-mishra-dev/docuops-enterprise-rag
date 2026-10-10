from app.rag.generator import generate_answer


def app(query: str, context: str):
    ans = generate_answer(query, context)
    print(ans)


if __name__ == "__main__":
    sample_context = "The work-from-home policy allows up to 2 days per week with manager approval."
    sample_query = "What is the work-from-home policy?"
    
    app(sample_query, sample_context)