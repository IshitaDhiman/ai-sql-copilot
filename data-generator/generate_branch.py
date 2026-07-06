from db_connection import get_connection
from faker_utils import random_city, random_phone, random_address
from config import NUMBER_OF_BRANCHES
from faker import Faker
import random

fake = Faker("en_IN")


def generate_branches(conn):

    cursor = conn.cursor()

    for i in range(1, NUMBER_OF_BRANCHES + 1):

        city, state, region = random_city()

        branch_code = f"BR{i:04d}"

        branch_name = f"{city} Branch"

        ifsc = f"AISQ{i:07d}"

        cursor.execute(
            """
            INSERT INTO banking.branch
            (
                branch_code,
                branch_name,
                ifsc_code,
                address,
                city,
                state,
                region,
                phone_number,
                opened_date,
                status
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                branch_code,
                branch_name,
                ifsc,
                random_address(),
                city,
                state,
                region,
                random_phone(),
                fake.date_between("-30y", "today"),
                "ACTIVE",
            ),
        )

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_BRANCHES} branches inserted successfully.")