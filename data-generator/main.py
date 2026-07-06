from generate_branch import generate_branches
from generate_employee import generate_employees
from generate_customer import generate_customers
from generate_account import generate_accounts
from generate_account_transaction import generate_account_transactions
from generate_loan import generate_loans
from generate_loan_emi import generate_loan_emis
from generate_credit_card import generate_credit_cards
from generate_card_transaction import generate_card_transactions
from generate_fd import generate_fixed_deposits
from generate_beneficiary import generate_beneficiaries
from generate_nominee import generate_nominees
from db_connection import get_connection


def main():
    conn = get_connection()
    print("Generating Branches...")
    # generate_branches(conn)

    print("Generating Employees...")
    #generate_employees(conn)

    print("Generating Customers...")
    #generate_customers(conn)

    print("Generating Accounts...")
    #generate_accounts(conn)

    print("Generating Transactions...")
    generate_account_transactions(conn)

    print("Generating Loans...")
    generate_loans()

    print("Generating EMIs...")
    generate_loan_emis()

    print("Generating Credit Cards...")
    generate_credit_cards()

    print("Generating Card Transactions...")
    generate_card_transactions()

    print("Generating Fixed Deposits...")
    generate_fixed_deposits()

    print("Generating Beneficiaries...")
    generate_beneficiaries()

    print("Generating Nominees...")
    generate_nominees()

    print("Data generation completed successfully.")


if __name__ == "__main__":
    main()