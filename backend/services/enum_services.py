from sqlalchemy import text

from database.connection import engine


def fetch_lookup_values():
    """
    Fetch commonly used lookup values from the database.
    These are injected into the prompt so the LLM uses
    the exact values stored in PostgreSQL.
    """

    queries = {
        "loan.loan_status": """
            SELECT DISTINCT loan_status
            FROM loan
            ORDER BY loan_status;
        """,

        "customer_segment.segment_name": """
            SELECT DISTINCT segment_name
            FROM customer_segment
            ORDER BY segment_name;
        """,

        "account.account_status": """
            SELECT DISTINCT account_status
            FROM account
            ORDER BY account_status;
        """,

        "loan_emi.payment_status": """
            SELECT DISTINCT payment_status
            FROM loan_emi
            ORDER BY payment_status;
        """
    }

    values = {}

    with engine.connect() as connection:

        for key, query in queries.items():

            result = connection.execute(text(query))

            values[key] = [
                str(row[0])
                for row in result
                if row[0] is not None
            ]

    return values


if __name__ == "__main__":

    from pprint import pprint

    pprint(fetch_lookup_values())