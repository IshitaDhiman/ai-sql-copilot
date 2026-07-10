import time

from sqlalchemy import text

from database.connection import engine

from utils.query_validator import validate_query


def execute_query(query: str):

    validate_query(query)

    start = time.perf_counter()

    with engine.connect() as connection:

        result = connection.execute(text(query))

        columns = list(result.keys())

        rows = [
            list(row)
            for row in result.fetchall()
        ]

    execution_time = round(
        (time.perf_counter() - start) * 1000,
        2
    )

    return {
        "columns": columns,
        "rows": rows,
        "row_count": len(rows),
        "execution_time_ms": execution_time,
    }