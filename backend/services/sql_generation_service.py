from services.prompt_builder import build_prompt
from services.llm_service import generate_sql


def generate_sql_from_question(question: str):
    """
    Generate SQL from a natural language question.
    """

    # Build prompt (this already fetches schema and RAG knowledge)
    prompt = build_prompt(question)

    # Generate SQL
    sql = generate_sql(prompt)

    return sql


if __name__ == "__main__":

    question = input("Question: ")

    sql = generate_sql_from_question(question)

    print("\nGenerated SQL")
    print("=" * 80)
    print(sql)