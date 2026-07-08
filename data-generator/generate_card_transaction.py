import random
import uuid

from faker import Faker

fake = Faker("en_IN")


MERCHANTS = {

    1: [
        "Amazon",
        "Flipkart",
        "Myntra",
        "Reliance Trends",
        "Croma"
    ],

    2: [
        "Swiggy",
        "Zomato",
        "Domino's",
        "KFC",
        "McDonald's"
    ],

    3: [
        "Indian Oil",
        "HP Petrol",
        "Bharat Petroleum",
        "Shell"
    ],

    4: [
        "IRCTC",
        "MakeMyTrip",
        "Uber",
        "IndiGo",
        "Air India"
    ],

    5: [
        "BESCOM",
        "Airtel",
        "Jio",
        "ACT Fibernet"
    ],

    6: [
        "Apollo Hospital",
        "Fortis",
        "PharmEasy",
        "1mg"
    ],

    7: [
        "BookMyShow",
        "Netflix",
        "PVR",
        "Spotify"
    ],

    8: [
        "Groww",
        "Zerodha",
        "Upstox",
        "Angel One"
    ],

    9: [
        "Coursera",
        "Udemy",
        "Unacademy",
        "BYJU'S"
    ],

    10: [
        "Local Merchant",
        "General Store",
        "Misc Purchase"
    ]

}


CATEGORY_AMOUNTS = {

    1: (500, 30000),
    2: (150, 3000),
    3: (500, 5000),
    4: (1000, 40000),
    5: (500, 10000),
    6: (300, 50000),
    7: (300, 5000),
    8: (1000, 100000),
    9: (1000, 100000),
    10: (100, 10000)

}


CITIES = [

    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad"

]


COUNTRIES = [

    "India",
    "India",
    "India",
    "India",
    "India",
    "India",
    "India",
    "India",
    "India",
    "India",
    "Singapore",
    "UAE",
    "USA",
    "United Kingdom"

]


def get_credit_cards(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            cc.card_id,
            cc.issue_date,
            ct.reward_rate,
            ct.card_type_name
        FROM banking.credit_card cc
        JOIN banking.card_type ct
            ON cc.card_type_id = ct.card_type_id
    """)

    cards = cursor.fetchall()

    cursor.close()

    return cards


def get_transaction_categories(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            transaction_category_id
        FROM banking.transaction_category
        WHERE is_active = TRUE
    """)

    categories = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return categories


def transaction_status():

    chance = random.random()

    if chance < 0.94:

        return "SUCCESS"

    elif chance < 0.97:

        return "FAILED"

    return "PENDING"


def transaction_count(card_type):

    if card_type == "Silver":

        return random.randint(25, 80)

    elif card_type == "Gold":

        return random.randint(40, 120)

    elif card_type == "Platinum":

        return random.randint(80, 180)

    return random.randint(120, 250)


def generate_reference():

    return "CC" + uuid.uuid4().hex.upper()[:22]

from config import NUMBER_OF_CARD_TRANSACTIONS


def generate_card_transactions(conn):

    cursor = conn.cursor()

    cards = get_credit_cards(conn)

    categories = get_transaction_categories(conn)

    transactions_generated = 0

    for card in cards:

        if transactions_generated >= NUMBER_OF_CARD_TRANSACTIONS:
            break

        card_id = card[0]
        issue_date = card[1]
        reward_rate = float(card[2])
        card_type = card[3]

        number_of_transactions = transaction_count(card_type)

        for _ in range(number_of_transactions):

            if transactions_generated >= NUMBER_OF_CARD_TRANSACTIONS:
                break

            category_id = random.choice(categories)

            merchant = random.choice(
                MERCHANTS[category_id]
            )

            minimum_amount, maximum_amount = CATEGORY_AMOUNTS[
                category_id
            ]

            amount = round(
                random.uniform(
                    minimum_amount,
                    maximum_amount
                ),
                2
            )

            status = transaction_status()

            if status == "SUCCESS":

                cashback = round(
                    amount * reward_rate / 100,
                    2
                )

            else:

                cashback = 0

            transaction_time = fake.date_time_between(
                start_date=issue_date,
                end_date="now"
            )

            country = random.choice(COUNTRIES)

            if country == "India":

                city = random.choice(CITIES)

            else:

                city = None

            cursor.execute(
                """
                INSERT INTO banking.card_transaction
                (
                    card_id,
                    transaction_reference,
                    transaction_category_id,
                    transaction_status,
                    amount,
                    merchant_name,
                    merchant_city,
                    merchant_country,
                    cashback_earned,
                    transaction_timestamp
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                )
                """,
                (
                    card_id,
                    generate_reference(),
                    category_id,
                    status,
                    amount,
                    merchant,
                    city,
                    country,
                    cashback,
                    transaction_time
                )
            )

            transactions_generated += 1

    conn.commit()

    cursor.close()

    print(
        f"{transactions_generated} card transactions inserted successfully."
    )