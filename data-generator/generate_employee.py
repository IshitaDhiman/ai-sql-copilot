import random

from faker import Faker

from config import NUMBER_OF_EMPLOYEES

fake = Faker("en_IN")

from faker_utils import (
    random_designation,
    random_salary,
    random_rating
)


def get_department_ids(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT department_id
        FROM banking.employee_department
        WHERE is_active = TRUE
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


def generate_employees(conn):

    cursor = conn.cursor()

    department_ids = get_department_ids(conn)

    branch_ids = get_branch_ids(conn)

    for i in range(1, NUMBER_OF_EMPLOYEES + 1):

        first_name = fake.first_name()

        last_name = fake.last_name()

        designation = random_designation()

        salary = random_salary(designation)

        cursor.execute(
            """
            INSERT INTO banking.employee
            (
                employee_code,
                first_name,
                last_name,
                email,
                phone_number,
                designation,
                department_id,
                salary,
                performance_rating,
                hire_date,
                manager_id,
                branch_id,
                status
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                f"EMP{i:06d}",
                first_name,
                last_name,
                f"{first_name.lower()}.{last_name.lower()}{random.randint(1,999)}@bank.com",
                fake.msisdn()[:10],
                designation,
                random.choice(department_ids),
                salary,
                random_rating(),
                fake.date_between(start_date="-20y", end_date="today"),
                None,
                random.choice(branch_ids),
                "ACTIVE",
            ),
        )

    conn.commit()

    cursor.close()

    print(f"{NUMBER_OF_EMPLOYEES} employees inserted successfully.")