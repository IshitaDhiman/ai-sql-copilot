FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
]


def validate_query(query: str):

    query = query.strip()

    upper_query = query.upper()

    if not (
        upper_query.startswith("SELECT")
        or upper_query.startswith("WITH")
    ):
        raise ValueError(
            "Only SELECT and WITH queries are allowed."
        )

    for keyword in FORBIDDEN_KEYWORDS:

        if keyword in upper_query:
            raise ValueError(
                f"{keyword} statements are not allowed."
            )

    return True