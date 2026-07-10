import random
from datetime import date

from faker import Faker

from config import NUMBER_OF_NOMINEES

fake = Faker("en_IN")


RELATIONSHIPS = [
    "Spouse",
    "Father",
    "Mother",
    "Son",
    "Daughter",
    "Brother",
    "Sister"
]


def get_customers(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customer_id
        FROM banking.customer
        WHERE customer_status='ACTIVE'
    """)

    customers = cursor.fetchall()

    cursor.close()

    return customers


def nominee_count():

    chance = random.random()

    if chance < 0.20:
        return 0

    elif chance < 0.90:
        return 1

    return 2


def nominee_dob(relationship):

    today = date.today()

    if relationship in ["Father", "Mother"]:

        age = random.randint(50, 80)

    elif relationship == "Spouse":

        age = random.randint(22, 65)

    elif relationship in ["Brother", "Sister"]:

        age = random.randint(18, 60)

    else:

        age = random.randint(1, 30)

    year = today.year - age

    month = random.randint(1, 12)

    day = random.randint(1, 28)

    return date(year, month, day)


def generate_nominees(conn):

    cursor = conn.cursor()

    customers = get_customers(conn)

    used_phone_numbers = set()

    inserted = 0

    for customer in customers:

        if inserted >= NUMBER_OF_NOMINEES:
            break

        customer_id = customer[0]

        count = nominee_count()

        if count == 0:
            continue

        relationships = random.sample(
            RELATIONSHIPS,
            count
        )

        for relationship in relationships:

            if inserted >= NUMBER_OF_NOMINEES:
                break

            while True:

                phone = fake.msisdn()[:10]

                if (
                    phone[0] in "6789"
                    and phone not in used_phone_numbers
                ):

                    used_phone_numbers.add(phone)

                    break

            cursor.execute(
                """
                INSERT INTO banking.customer_nominee
                (
                    customer_id,
                    nominee_name,
                    relationship,
                    date_of_birth,
                    phone_number
                )
                VALUES
                (
                    %s,%s,%s,%s,%s
                )
                """,
                (
                    customer_id,
                    fake.name(),
                    relationship,
                    nominee_dob(relationship),
                    phone
                )
            )

            inserted += 1

    conn.commit()

    cursor.close()

    print(f"{inserted} nominees inserted successfully.")