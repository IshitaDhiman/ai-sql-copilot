import random

from faker import Faker

from config import NUMBER_OF_FIXED_DEPOSITS

fake = Faker("en_IN")


def get_customers(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            annual_income
        FROM banking.customer
        WHERE customer_status='ACTIVE'
    """)

    customers = cursor.fetchall()

    cursor.close()

    return customers


def get_interest_rate(tenure):

    if tenure <= 12:
        return 6.50

    elif tenure <= 24:
        return 6.90

    elif tenure <= 36:
        return 7.10

    elif tenure <= 60:
        return 7.30

    return 7.50


def calculate_maturity(principal, rate, tenure):

    years = tenure / 12

    maturity = principal + (
        principal * rate * years / 100
    )

    return round(maturity, 2)


def generate_fixed_deposits(conn):

    cursor = conn.cursor()

    customers = get_customers(conn)

    payouts = [
        "Monthly",
        "Quarterly",
        "At Maturity"
    ]

    tenures = [
        6,
        12,
        24,
        36,
        60
    ]

    generated = 0

    for customer in customers:

        if generated >= NUMBER_OF_FIXED_DEPOSITS:
            break

        customer_id = customer[0]
        income = customer[1] or 0

        probability = random.random()

        if probability < 0.55:
            continue

        if probability < 0.90:
            fd_count = 1
        elif probability < 0.98:
            fd_count = 2
        else:
            fd_count = 3

        for _ in range(fd_count):

            if generated >= NUMBER_OF_FIXED_DEPOSITS:
                break

            if income < 500000:

                principal = random.randint(
                    10000,
                    100000
                )

            elif income < 1500000:

                principal = random.randint(
                    50000,
                    500000
                )

            else:

                principal = random.randint(
                    100000,
                    2000000
                )

            tenure = random.choice(tenures)

            interest_rate = get_interest_rate(tenure)

            maturity_amount = calculate_maturity(
                principal,
                interest_rate,
                tenure
            )

            start_date = fake.date_between(
                start_date="-8y",
                end_date="-30d"
            )

            maturity_date = fake.date_between(
                start_date=start_date,
                end_date="today"
            )

            try:

                maturity_date = start_date.replace(
                    year=start_date.year + (tenure // 12)
                )

            except ValueError:

                maturity_date = start_date.replace(
                    month=2,
                    day=28,
                    year=start_date.year + (tenure // 12)
                )

            if maturity_date < fake.date_object():

                status = "MATURED"

            else:

                status = "ACTIVE"

            cursor.execute(
                """
                INSERT INTO banking.fixed_deposit
                (
                    customer_id,
                    principal_amount,
                    interest_rate,
                    tenure_months,
                    maturity_amount,
                    interest_payout,
                    start_date,
                    maturity_date,
                    status
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    customer_id,
                    principal,
                    interest_rate,
                    tenure,
                    maturity_amount,
                    random.choice(payouts),
                    start_date,
                    maturity_date,
                    status
                )
            )

            generated += 1

    conn.commit()

    cursor.close()

    print(f"{generated} fixed deposits inserted successfully.")