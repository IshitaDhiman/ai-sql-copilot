import random
from datetime import date

from faker import Faker

fake = Faker("en_IN")


def get_customers(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            annual_income
        FROM banking.customer
        WHERE customer_status = 'ACTIVE'
    """)

    customers = cursor.fetchall()

    cursor.close()

    return customers


def get_card_types(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            card_type_id,
            card_type_name,
            annual_fee,
            reward_rate
        FROM banking.card_type
        WHERE is_active = TRUE
    """)

    rows = cursor.fetchall()

    cursor.close()

    card_types = {}

    for row in rows:

        card_types[row[1]] = {
            "id": row[0],
            "annual_fee": float(row[2]),
            "reward_rate": float(row[3])
        }

    return card_types


def eligible_card_types(income):

    if income is None:
        income = 0

    if income < 400000:

        return ["Silver"]

    elif income < 1000000:

        return [
            "Silver",
            "Gold"
        ]

    elif income < 2500000:

        return [
            "Gold",
            "Platinum"
        ]

    else:

        return [
            "Gold",
            "Platinum",
            "Signature"
        ]


def cards_to_issue():

    chance = random.random()

    if chance < 0.45:

        return 0

    elif chance < 0.85:

        return 1

    elif chance < 0.97:

        return 2

    else:

        return 3


def credit_limit(card_type):

    limits = {

        "Silver": (
            25000,
            75000
        ),

        "Gold": (
            75000,
            200000
        ),

        "Platinum": (
            200000,
            500000
        ),

        "Signature": (
            500000,
            1500000
        )

    }

    low, high = limits[card_type]

    return random.randint(low, high)


def reward_program(card_type):

    mapping = {

        "Silver": [
            "Cashback Rewards",
            "Shopping Rewards"
        ],

        "Gold": [
            "Travel Rewards",
            "Dining Rewards",
            "Shopping Rewards"
        ],

        "Platinum": [
            "Premium Lifestyle",
            "Travel Elite"
        ],

        "Signature": [
            "Luxury Privileges",
            "Global Rewards"
        ]

    }

    return random.choice(mapping[card_type])


def generate_card_number():

    while True:

        number = "".join(
            random.choices(
                "0123456789",
                k=16
            )
        )

        if number[0] != "0":
            return number


def card_status(expiry_date):

    today = date.today()

    if expiry_date < today:
        return "EXPIRED"

    if random.random() < 0.05:
        return "BLOCKED"

    return "ACTIVE"
from config import NUMBER_OF_CREDIT_CARDS


def generate_credit_cards(conn):

    cursor = conn.cursor()

    customers = get_customers(conn)

    card_types = get_card_types(conn)

    used_card_numbers = set()

    cards_generated = 0

    for customer in customers:

        customer_id = customer[0]
        annual_income = customer[1]

        eligible_cards = eligible_card_types(annual_income)

        number_of_cards = min(
            cards_to_issue(),
            len(eligible_cards)
        )

        if number_of_cards == 0:
            continue

        selected_card_types = random.sample(
            eligible_cards,
            number_of_cards
        )

        for card_name in selected_card_types:

            if cards_generated >= NUMBER_OF_CREDIT_CARDS:
                break

            card = card_types[card_name]

            limit = credit_limit(card_name)

            utilized_amount = round(
                random.uniform(
                    0,
                    limit * 0.80
                ),
                2
            )

            available_limit = round(
                limit - utilized_amount,
                2
            )

            issue_date = fake.date_between(
                start_date="-5y",
                end_date="-30d"
            )

            try:

                expiry_date = issue_date.replace(
                    year=issue_date.year + 5
                )

            except ValueError:

                expiry_date = issue_date.replace(
                    month=2,
                    day=28,
                    year=issue_date.year + 5
                )

            while True:

                card_number = generate_card_number()

                if card_number not in used_card_numbers:

                    used_card_numbers.add(card_number)

                    break

            billing_cycle = random.randint(1, 28)

            cursor.execute(
                """
                INSERT INTO banking.credit_card
                (
                    customer_id,
                    card_type_id,
                    card_number,
                    reward_program,
                    credit_limit,
                    available_limit,
                    annual_fee,
                    cashback_percentage,
                    billing_cycle,
                    issue_date,
                    expiry_date,
                    card_status
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                )
                """,
                (
                    customer_id,
                    card["id"],
                    card_number,
                    reward_program(card_name),
                    limit,
                    available_limit,
                    card["annual_fee"],
                    card["reward_rate"],
                    billing_cycle,
                    issue_date,
                    expiry_date,
                    card_status(expiry_date)
                )
            )

            cards_generated += 1

        if cards_generated >= NUMBER_OF_CREDIT_CARDS:
            break

    conn.commit()

    cursor.close()

    print(f"{cards_generated} credit cards inserted successfully.")