from app.rag.retriever import retrieve_relevant_chunks
from services.schema_service import fetch_schema
from services.enum_services import fetch_lookup_values


def format_schema(schema: dict) -> str:
    """
    Converts schema into an LLM-friendly format.
    """

    schema_text = "AVAILABLE DATABASE TABLES\n\n"

    for table_name in sorted(schema.keys()):

        schema_text += f"Table: {table_name}\n"
        schema_text += "Columns:\n"

        for column in schema[table_name]:

            schema_text += (
                f"   - {column['column']} ({column['type']})\n"
            )

        schema_text += "\n----------------------------------------\n\n"

    return schema_text


def format_knowledge(chunks: list) -> str:

    if not chunks:
        return "No additional business knowledge found."

    knowledge = ""

    for chunk in chunks:

        knowledge += (
            f"[{chunk['document_name']} -> {chunk['section_name']}]\n"
        )

        knowledge += chunk["content"]

        knowledge += "\n\n"

    return knowledge

def format_lookup_values(values: dict) -> str:
    """
    Formats lookup/enum values for the LLM prompt.
    """

    if not values:
        return "No lookup values found."

    text = ""

    for key, items in values.items():

        text += f"{key}\n"

        for item in items:
            text += f"   - {item}\n"

        text += "\n"

    return text

def build_prompt(question: str) -> str:

    schema = fetch_schema()
    lookup_values = fetch_lookup_values()

    chunks = retrieve_relevant_chunks(
        question,
        top_k=5
    )

    schema_text = format_schema(schema)

    knowledge_text = format_knowledge(chunks)
    lookup_text = format_lookup_values(lookup_values)

    prompt = f"""
You are an expert PostgreSQL SQL Developer.

Your job is to convert banking questions into PostgreSQL SQL.

=========================================================
STRICT RULES
=========================================================

1. Return ONLY SQL.

2. Never explain your answer.

3. Never use Markdown.

4. Never wrap SQL inside ```.

5. Never output anything except SQL.

6. ONLY use tables listed below.

7. NEVER invent tables.

8. NEVER invent columns.

9. NEVER pluralize table names.

Example:

Correct:
customer
loan
account
loan_emi

Wrong:
customers
loans
accounts

10. ONLY use columns that exist.

11. Use JOIN whenever relationships are required.

12. Always qualify columns with table aliases.

Good aliases:

customer c
loan l
loan_emi le
account a
branch b
customer_segment cs
credit_card cc

13. Use PostgreSQL syntax.

14. Prefer explicit JOINs.

15. Use business knowledge whenever applicable.

16. If filtering on lookup or enum columns, ALWAYS use one of the values listed in the LOOKUP / ENUM VALUES section.

17. Never guess lookup or enum values.

=========================================================
BANKING KNOWLEDGE
=========================================================

{knowledge_text}

=========================================================
DATABASE SCHEMA
=========================================================

{schema_text}

=========================================================
LOOKUP / ENUM VALUES
=========================================================

The following columns contain fixed values stored in the database.

When filtering on these columns:

- Always use one of the values exactly as written.
- Never change the capitalization.
- Never invent new values.

{lookup_text}

=========================================================
EXAMPLES
=========================================================

Question:
List customers with credit score above 750

SQL:
SELECT
    customer_id,
    first_name,
    last_name,
    credit_score
FROM customer
WHERE credit_score > 750;

----------------------------------------

Question:
Show all active loans

SQL:
SELECT
    loan_id,
    customer_id,
    sanctioned_amount,
    outstanding_amount
FROM loan
WHERE loan_status = 'ACTIVE';

----------------------------------------

Question:
Show premium customers

SQL:
SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customer c
JOIN customer_segment cs
ON c.customer_segment_id = cs.customer_segment_id
WHERE cs.segment_name = 'Premium';

----------------------------------------

Question:
Show premium customers with active loans

SQL:
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    l.loan_id,
    l.outstanding_amount
FROM customer c
JOIN customer_segment cs
ON c.customer_segment_id = cs.customer_segment_id
JOIN loan l
ON c.customer_id = l.customer_id
WHERE cs.segment_name = 'Premium'
AND l.loan_status = 'ACTIVE';

=========================================================
USER QUESTION
=========================================================

{question}

=========================================================
OUTPUT
=========================================================

Return ONLY the SQL query.
"""

    return prompt


if __name__ == "__main__":

    question = input("Question: ")

    print(build_prompt(question))