from sqlalchemy import text

from database.connection import engine


def fetch_schema():

    query = """
        SELECT
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'banking'
        ORDER BY table_name,
                 ordinal_position
    """

    with engine.connect() as connection:

        result = connection.execute(text(query))

        schema = {}

        for row in result:

            table = row.table_name

            if table not in schema:
                schema[table] = []

            schema[table].append(
                {
                    "column": row.column_name,
                    "type": row.data_type
                }
            )

    return schema