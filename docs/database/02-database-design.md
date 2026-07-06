# Database Design

## Database Type

Relational Database (PostgreSQL)

---

## Design Principles

- Third Normal Form (3NF)
- Surrogate Primary Keys
- Foreign Key Relationships
- Minimal Data Redundancy
- Consistent Naming Convention

---

## Core Entities

- Customer
- Branch
- Employee
- Account
- Account Transaction
- Loan
- Loan EMI
- Credit Card
- Card Transaction
- Fixed Deposit
- Customer Beneficiary
- Customer Nominee

---

## Relationships

Customer
- Account
- Loan
- Credit Card
- Fixed Deposit

Branch
- Employee
- Account
- Loan

Account
- Account Transaction

Loan
- Loan EMI

Credit Card
- Card Transaction

---

## Naming Convention

Tables use snake_case.

Primary Keys:

customer_id

Foreign Keys:

customer_id

Audit Columns:

created_at

updated_at