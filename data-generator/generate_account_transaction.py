import random
import uuid

from faker import Faker

from config import NUMBER_OF_TRANSACTIONS

fake = Faker("en_IN")


def get_accounts(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT account_id
        FROM banking.account
        WHERE account_status = 'ACTIVE'
    """)

    accounts = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return accounts


def get_transaction_categories(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT transaction_category_id
        FROM banking.transaction_category
        WHERE is_active = TRUE
    """)

    categories = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return categories


def random_transaction_amount():

    return round(random.uniform(100, 50000), 2)


def random_payment_mode():

    return random.choice([
        "UPI",
        "NEFT",
        "RTGS",
        "IMPS",
        "CARD",
        "CASH",
        "CHEQUE"
    ])


def random_transaction_type():

    return random.choice([
        "CREDIT",
        "DEBIT"
    ])


def random_transaction_status():

    return random.choice([
        "SUCCESS",
        "FAILED",
        "PENDING"
    ])


def random_merchant():

    merchants = [
        "Amazon",
        "Flipkart",
        "Swiggy",
        "Zomato",
        "Reliance Fresh",
        "DMart",
        "Apollo Pharmacy",
        "IRCTC",
        "Uber",
        "Ola",
        "Salary Credit",
        "Electricity Board"
    ]

    return random.choice(merchants)


def generate_account_transactions(conn):

    cursor = conn.cursor()

    accounts = get_accounts(conn)

    categories = get_transaction_categories(conn)

    for i in range(NUMBER_OF_TRANSACTIONS):

        cursor.execute(
            """
            INSERT INTO banking.account_transaction
            (
                account_id,
                transaction_reference,
                transaction_type,
                payment_mode,
                transaction_category_id,
                transaction_status,
                amount,
                currency,
                merchant_name,
                remarks,
                transaction_timestamp
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                random.choice(accounts),
                "TXN" + uuid.uuid4().hex[:20].upper(),
                random_transaction_type(),
                random_payment_mode(),
                random.choice(categories),
                random_transaction_status(),
                random_transaction_amount(),
                "INR",
                random_merchant(),
                fake.sentence(nb_words=5),
                fake.date_time_between(
                    start_date="-3y",
                    end_date="now"
                )
            )
        )

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_TRANSACTIONS} account transactions inserted successfully.")