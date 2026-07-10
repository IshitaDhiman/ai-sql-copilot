import random

from faker import Faker

from config import NUMBER_OF_LOANS

fake = Faker("en_IN")


def get_customer_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id
        FROM banking.customer
        WHERE customer_status = 'ACTIVE'
    """)

    customers = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return customers


def get_branch_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT branch_id
        FROM banking.branch
    """)

    branches = [row[0] for row in cursor.fetchall()]

    cursor.close()

    return branches


def get_loan_types(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            loan_type_id,
            loan_type_name,
            maximum_tenure_months
        FROM banking.loan_type
        WHERE is_active = TRUE
    """)

    loan_types = cursor.fetchall()

    cursor.close()

    return loan_types


def get_interest_rate(loan_type_name):

    rates = {
        "Home Loan": 8.50,
        "Personal Loan": 13.50,
        "Car Loan": 9.25,
        "Education Loan": 10.00,
        "Gold Loan": 8.75
    }

    return rates.get(loan_type_name, 10.00)


def calculate_emi(principal, annual_rate, months):

    monthly_rate = annual_rate / (12 * 100)

    emi = (
        principal
        * monthly_rate
        * pow(1 + monthly_rate, months)
    ) / (
        pow(1 + monthly_rate, months) - 1
    )

    return round(emi, 2)


def generate_loans(conn):

    cursor = conn.cursor()

    customers = get_customer_ids(conn)

    branches = get_branch_ids(conn)

    loan_types = get_loan_types(conn)

    collateral_types = [
        "Property",
        "Vehicle",
        "Gold",
        "Fixed Deposit",
        "None"
    ]

    standard_tenures = [12, 24, 36, 60, 84, 120, 180, 240, 360]

    for _ in range(NUMBER_OF_LOANS):

        customer_id = random.choice(customers)

        branch_id = random.choice(branches)

        loan_type = random.choice(loan_types)

        loan_type_id = loan_type[0]
        loan_type_name = loan_type[1]
        maximum_tenure = loan_type[2]

        interest_rate = get_interest_rate(loan_type_name)

        possible_tenures = [
            t for t in standard_tenures
            if t <= maximum_tenure
        ]

        if maximum_tenure not in possible_tenures:
            possible_tenures.append(maximum_tenure)

        tenure = random.choice(possible_tenures)

        sanctioned_amount = random.randint(100000, 5000000)

        disbursed_amount = sanctioned_amount

        outstanding_amount = round(
            sanctioned_amount * random.uniform(0.20, 1.00),
            2
        )

        emi = calculate_emi(
            sanctioned_amount,
            interest_rate,
            tenure
        )

        processing_fee = round(
            sanctioned_amount * 0.01,
            2
        )

        approval_date = fake.date_between(
            start_date="-10y",
            end_date="-30d"
        )

        if random.random() < 0.15:

            closure_date = fake.date_between(
                start_date=approval_date,
                end_date="today"
            )

            loan_status = "CLOSED"

        else:

            closure_date = None

            loan_status = "ACTIVE"

        cursor.execute(
            """
            INSERT INTO banking.loan
            (
                customer_id,
                branch_id,
                loan_type_id,
                sanctioned_amount,
                disbursed_amount,
                outstanding_amount,
                interest_rate,
                tenure_months,
                emi_amount,
                processing_fee,
                collateral_type,
                approval_date,
                closure_date,
                loan_status
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                customer_id,
                branch_id,
                loan_type_id,
                sanctioned_amount,
                disbursed_amount,
                outstanding_amount,
                interest_rate,
                tenure,
                emi,
                processing_fee,
                random.choice(collateral_types),
                approval_date,
                closure_date,
                loan_status
            )
        )

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_LOANS} loans inserted successfully.")