from app.rag.retriever import retrieve_relevant_chunks
from services.schema_service import fetch_schema


def build_rag_context(user_question: str):
    """
    Build the context that will be sent to the LLM.
    """

    knowledge = retrieve_relevant_chunks(user_question)

    schema = fetch_schema()

    return {
        "question": user_question,
        "knowledge": knowledge,
        "schema": schema
    }


if __name__ == "__main__":

    question = input("Question: ")

    context = build_rag_context(question)

    print("\nQUESTION")
    print("-" * 80)
    print(context["question"])

    print("\nKNOWLEDGE")
    print("-" * 80)

    for chunk in context["knowledge"]:

        print(f"\n[{chunk['document_name']} - {chunk['section_name']}]")
        print(chunk["content"][:300])

    print("\nSCHEMA")
    print("-" * 80)

    for table, columns in context["schema"].items():

        print(f"\n{table}")

        for column in columns:

            print(
                f"   {column['column']} ({column['type']})"
            )