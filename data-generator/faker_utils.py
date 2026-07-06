from faker import Faker
import random
import string
generated_pan = set()
generated_aadhaar = set()

fake = Faker("en_IN")
INDIAN_CITIES = [
    ("Bengaluru", "Karnataka", "South"),
    ("Mumbai", "Maharashtra", "West"),
    ("Delhi", "Delhi", "North"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Pune", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Kolkata", "West Bengal", "East"),
    ("Jaipur", "Rajasthan", "North"),
    ("Lucknow", "Uttar Pradesh", "North"),
]


DESIGNATIONS = {
    "Branch Manager": (120000, 180000),
    "Assistant Manager": (80000, 120000),
    "Relationship Manager": (60000, 90000),
    "Loan Officer": (50000, 80000),
    "Customer Service Executive": (30000, 50000),
    "Cashier": (25000, 40000),
    "Operations Executive": (40000, 70000),
    "IT Support Engineer": (60000, 100000),
    "Credit Analyst": (70000, 110000),
    "Sales Executive": (35000, 60000)
}
OCCUPATIONS = {
    "Software Engineer": (800000, 2500000),
    "Doctor": (1200000, 4000000),
    "Teacher": (400000, 1000000),
    "Business Owner": (1000000, 5000000),
    "Government Employee": (500000, 1500000),
    "Student": (0, 200000),
    "Retired": (200000, 800000),
    "Chartered Accountant": (900000, 2500000),
    "Lawyer": (1000000, 3000000),
    "Sales Executive": (300000, 900000)
}

def random_account_balance(account_type_name):
    if account_type_name == "Savings":
        return round(random.uniform(5000, 500000), 2)

    elif account_type_name == "Salary":
        return round(random.uniform(1000, 200000), 2)

    elif account_type_name == "Current":
        return round(random.uniform(50000, 2500000), 2)

    elif account_type_name == "NRI":
        return round(random.uniform(25000, 1000000), 2)

    return round(random.uniform(1000, 100000), 2)

def random_gender():
    return random.choice(["MALE", "FEMALE"])


def random_occupation():
    return random.choice(list(OCCUPATIONS.keys()))


def random_income(occupation):
    low, high = OCCUPATIONS[occupation]
    return random.randint(low, high)


def random_dob():
    return fake.date_between(start_date="-70y", end_date="-18y")


def generate_pan():
    while True:
        pan = (
            ''.join(random.choices(string.ascii_uppercase, k=5))
            + ''.join(random.choices(string.digits, k=4))
            + random.choice(string.ascii_uppercase)
        )

        if pan not in generated_pan:
            generated_pan.add(pan)
            return pan


def generate_aadhaar():
    while True:
        aadhaar = ''.join(random.choices(string.digits, k=12))

        if aadhaar not in generated_aadhaar:
            generated_aadhaar.add(aadhaar)
            return aadhaar

def random_designation():
    return random.choice(list(DESIGNATIONS.keys()))

def random_salary(designation):
    low, high = DESIGNATIONS[designation]
    return random.randint(low, high)

def random_rating():
    return round(random.uniform(3.0, 5.0), 2)

def random_city():
    return random.choice(INDIAN_CITIES)

def get_name():
    return fake.first_name(), fake.last_name()

def get_email(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}{random.randint(1,999)}@gmail.com"

def get_phone():
    return fake.msisdn()[:10]

def get_city():
    return fake.city()

def get_state():
    return fake.state()

def get_address():
    return fake.address().replace("\n", ", ")
def random_phone():
    return "9" + "".join(str(random.randint(0, 9)) for _ in range(9))

def random_address():
    return fake.address().replace("\n", ", ")