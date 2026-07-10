import random
from datetime import timedelta

from dateutil.relativedelta import relativedelta


def get_loans(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            loan_id,
            approval_date,
            tenure_months,
            emi_amount,
            loan_status
        FROM banking.loan
    """)

    loans = cursor.fetchall()

    cursor.close()

    return loans


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


def generate_loan_emis(conn):

    cursor = conn.cursor()

    loans = get_loans(conn)

    for loan in loans:

        loan_id = loan[0]
        approval_date = loan[1]
        tenure = loan[2]
        emi_amount = loan[3]
        loan_status = loan[4]

        first_due_date = approval_date + relativedelta(months=1)

        for installment_number in range(1, tenure + 1):

            due_date = first_due_date + relativedelta(
                months=installment_number - 1
            )

            today = due_date.today()

            # Future EMI
            if due_date > today:

                payment_status = "PENDING"
                paid_date = None
                delay_days = 0
                penalty = 0
                payment_mode = None

            else:

                # Closed loans
                if loan_status == "CLOSED":

                    payment_status = "PAID"

                else:

                    chance = random.random()

                    if chance < 0.80:
                        payment_status = "PAID"
                    elif chance < 0.95:
                        payment_status = "PENDING"
                    else:
                        payment_status = "OVERDUE"

                if payment_status == "PAID":

                    delay_days = random.randint(0, 5)

                    paid_date = due_date + timedelta(days=delay_days)

                    penalty = 0

                    payment_mode = random_payment_mode()

                elif payment_status == "OVERDUE":

                    delay_days = random.randint(5, 30)

                    paid_date = None

                    penalty = delay_days * 100

                    payment_mode = None

                else:

                    paid_date = None
                    delay_days = 0
                    penalty = 0
                    payment_mode = None

            cursor.execute(
                """
                INSERT INTO banking.loan_emi
                (
                    loan_id,
                    installment_number,
                    due_date,
                    amount,
                    penalty,
                    payment_mode,
                    paid_date,
                    delay_days,
                    payment_status
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    loan_id,
                    installment_number,
                    due_date,
                    emi_amount,
                    penalty,
                    payment_mode,
                    paid_date,
                    delay_days,
                    payment_status
                )
            )

    conn.commit()

    cursor.close()

    print("Loan EMI generation completed.")