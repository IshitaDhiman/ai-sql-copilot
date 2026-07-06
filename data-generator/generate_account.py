import random
from faker import Faker

from config import NUMBER_OF_ACCOUNTS
from faker_utils import random_account_balance

fake = Faker("en_IN")


def get_customer_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id
        FROM banking.customer
        WHERE customer_status = 'ACTIVE'
    """)

    ids = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return ids


def get_branch_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT branch_id
        FROM banking.branch
    """)

    ids = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return ids


def get_account_types(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            account_type_id,
            account_type_name,
            minimum_balance,
            interest_rate
        FROM banking.account_type
        WHERE is_active = TRUE
    """)

    rows = cursor.fetchall()

    cursor.close()

    return rows


def generate_accounts(conn):

    cursor = conn.cursor()

    customers = get_customer_ids(conn)

    branches = get_branch_ids(conn)

    account_types = get_account_types(conn)

    used_account_numbers = set()

    for i in range(1, NUMBER_OF_ACCOUNTS + 1):

        while True:

            account_number = ''.join(random.choices("0123456789", k=14))

            if account_number not in used_account_numbers:
                used_account_numbers.add(account_number)
                break

        customer_id = random.choice(customers)

        branch_id = random.choice(branches)

        account_type = random.choice(account_types)

        account_type_id = account_type[0]
        account_type_name = account_type[1]
        minimum_balance = account_type[2]
        interest_rate = account_type[3]

        balance = random_account_balance(account_type_name)

        available_balance = balance

        opened_date = fake.date_between(
            start_date="-15y",
            end_date="today"
        )

        cursor.execute(
            """
            INSERT INTO banking.account
            (
                account_number,
                customer_id,
                branch_id,
                account_type_id,
                balance,
                available_balance,
                minimum_balance,
                interest_rate,
                currency,
                opened_date,
                account_status
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                account_number,
                customer_id,
                branch_id,
                account_type_id,
                balance,
                available_balance,
                minimum_balance,
                interest_rate,
                "INR",
                opened_date,
                "ACTIVE"
            )
        )

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_ACCOUNTS} accounts inserted successfully.")