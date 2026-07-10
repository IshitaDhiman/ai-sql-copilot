import random

from faker import Faker

from config import NUMBER_OF_BENEFICIARIES

fake = Faker("en_IN")


def get_customers(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            customer_since
        FROM banking.customer
        WHERE customer_status = 'ACTIVE'
    """)

    customers = cursor.fetchall()

    cursor.close()

    return customers


def get_banks(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            bank_id,
            bank_name
        FROM banking.bank
        WHERE is_active = TRUE
    """)

    banks = cursor.fetchall()

    cursor.close()

    return banks


IFSC_PREFIX = {

    "State Bank of India": "SBIN",
    "HDFC Bank": "HDFC",
    "ICICI Bank": "ICIC",
    "Axis Bank": "UTIB",
    "Punjab National Bank": "PUNB",
    "Canara Bank": "CNRB",
    "Bank of Baroda": "BARB",
    "Kotak Mahindra Bank": "KKBK",
    "IndusInd Bank": "INDB",
    "Yes Bank": "YESB"

}


def generate_account_number():

    return "".join(
        random.choices(
            "0123456789",
            k=14
        )
    )


def generate_ifsc(bank_name):

    prefix = IFSC_PREFIX.get(bank_name, "BANK")

    return prefix + str(random.randint(100000, 999999))


def generate_beneficiaries(conn):

    cursor = conn.cursor()

    customers = get_customers(conn)

    banks = get_banks(conn)

    used_accounts = set()

    inserted = 0

    for customer_id, customer_since in customers:

        if inserted >= NUMBER_OF_BENEFICIARIES:
            break

        probability = random.random()

        if probability < 0.35:
            continue

        if probability < 0.75:
            beneficiary_count = random.randint(1, 2)

        elif probability < 0.93:
            beneficiary_count = random.randint(3, 5)

        else:
            beneficiary_count = random.randint(6, 8)

        for _ in range(beneficiary_count):

            if inserted >= NUMBER_OF_BENEFICIARIES:
                break

            bank_id, bank_name = random.choice(banks)

            while True:

                account_number = generate_account_number()

                if account_number not in used_accounts:
                    used_accounts.add(account_number)
                    break

            beneficiary_name = fake.name()

            nickname = random.choice(
                [
                    None,
                    "Family",
                    "Friend",
                    "Office",
                    "Self",
                    beneficiary_name.split()[0]
                ]
            )

            added_date = fake.date_between(
                start_date=customer_since,
                end_date="today"
            )

            cursor.execute(
                """
                INSERT INTO banking.customer_beneficiary
                (
                    customer_id,
                    bank_id,
                    beneficiary_name,
                    account_number,
                    ifsc_code,
                    nickname,
                    added_date
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s
                )
                """,
                (
                    customer_id,
                    bank_id,
                    beneficiary_name,
                    account_number,
                    generate_ifsc(bank_name),
                    nickname,
                    added_date
                )
            )

            inserted += 1

    conn.commit()

    cursor.close()

    print(f"{inserted} beneficiaries inserted successfully.")