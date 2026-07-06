import random

from faker import Faker

from config import NUMBER_OF_CUSTOMERS

from faker_utils import (
    random_gender,
    random_occupation,
    random_income,
    random_dob,
    generate_pan,
    generate_aadhaar
)

fake = Faker("en_IN")


def get_segment_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_segment_id
        FROM banking.customer_segment
        WHERE is_active = TRUE
    """)

    ids = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return ids


def get_risk_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT risk_category_id
        FROM banking.risk_category
        WHERE is_active = TRUE
    """)

    ids = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return ids


def generate_customers(conn):

    cursor = conn.cursor()

    segment_ids = get_segment_ids(conn)
    risk_ids = get_risk_ids(conn)

    for i in range(1, NUMBER_OF_CUSTOMERS + 1):

        first_name = fake.first_name()

        last_name = fake.last_name()

        occupation = random_occupation()

        income = random_income(occupation)

        cursor.execute("""
            INSERT INTO banking.customer
            (
                customer_code,
                first_name,
                last_name,
                date_of_birth,
                gender,
                email,
                phone_number,
                pan_number,
                aadhaar_number,
                occupation,
                annual_income,
                customer_segment_id,
                credit_score,
                risk_category_id,
                city,
                state,
                customer_since,
                customer_status
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            f"CUS{i:06d}",
            first_name,
            last_name,
            random_dob(),
            random_gender(),
            f"{first_name.lower()}.{last_name.lower()}{random.randint(1,9999)}@gmail.com",
            fake.msisdn()[:10],
            generate_pan(),
            generate_aadhaar(),
            occupation,
            income,
            random.choice(segment_ids),
            random.randint(300,900),
            random.choice(risk_ids),
            fake.city(),
            fake.state(),
            fake.date_between(start_date="-15y", end_date="today"),
            "ACTIVE"
        ))

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_CUSTOMERS} customers inserted successfully.")