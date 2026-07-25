from services.sql_generation_service import generate_sql_from_question
from services.query_service import execute_query


def ask_database(question: str):
    """
    Complete AI SQL Pipeline

    Question
        ↓
    Generate SQL
        ↓
    Execute SQL
        ↓
    Return Results
    """

    # Generate SQL
    generated_sql = generate_sql_from_question(question)

    # Execute SQL
    result = execute_query(generated_sql)

    return {
        "question": question,
        "generated_sql": generated_sql,
        "columns": result["columns"],
        "rows": result["rows"],
        "row_count": result["row_count"],
        "execution_time_ms": result["execution_time_ms"]
    }


if __name__ == "__main__":

    while True:

        question = input("\nAsk (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        try:

            response = ask_database(question)

            print("\nGenerated SQL")
            print("=" * 80)
            print(response["generated_sql"])

            print("\nRows Returned :", response["row_count"])
            print("Execution Time:", response["execution_time_ms"], "ms")

            if response["columns"]:

                print("\nColumns")
                print("-" * 80)
                print(" | ".join(response["columns"]))

                print("\nData")
                print("-" * 80)

                for row in response["rows"][:10]:
                    print(row)

                if response["row_count"] > 10:
                    print(f"\nShowing first 10 of {response['row_count']} rows.")

        except Exception as e:

            print("\nError")
            print("=" * 80)
            print(e)