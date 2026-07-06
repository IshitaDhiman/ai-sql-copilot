# Data Dictionary

## Customer

Stores customer information.

Primary Key:
- customer_id

Important Columns:

- customer_code
- first_name
- last_name
- annual_income
- credit_score
- city
- state
- customer_status

---

## Branch

Stores branch information.

Primary Key:
- branch_id

---

## Employee

Stores employee details.

Primary Key:
- employee_id

Foreign Keys:

- branch_id
- manager_id

---

## Account

Stores customer bank accounts.

Primary Key:

- account_id

Foreign Keys

- customer_id
- branch_id

---

## Account Transaction

Stores account transactions.

Primary Key

- transaction_id

Foreign Key

- account_id

---

## Loan

Stores customer loans.

Primary Key

- loan_id

Foreign Keys

- customer_id
- branch_id

---

## Loan EMI

Stores EMI details.

Primary Key

- emi_id

Foreign Key

- loan_id

---

## Credit Card

Stores customer credit cards.

Primary Key

- card_id

Foreign Key

- customer_id

---

## Card Transaction

Stores card purchases.

Primary Key

- card_transaction_id

Foreign Key

- card_id

---

## Fixed Deposit

Stores FD details.

Primary Key

- fd_id

Foreign Key

- customer_id

---

## Customer Beneficiary

Stores beneficiary details.

Primary Key

- beneficiary_id

Foreign Key

- customer_id

---

## Customer Nominee

Stores nominee details.

Primary Key

- nominee_id

Foreign Key

- customer_id