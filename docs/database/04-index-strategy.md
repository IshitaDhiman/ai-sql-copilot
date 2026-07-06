# Index Strategy

## Primary Indexes

Every table uses a Primary Key index.

Examples:

- customer_id
- account_id
- loan_id

---

## Secondary Indexes

Customer

- customer_code
- email
- phone_number
- pan_number

Account

- account_number
- customer_id

Loan

- customer_id
- status

Transaction

- account_id
- transaction_timestamp

Credit Card

- card_number

---

## Benefits

- Faster searches
- Faster joins
- Improved reporting queries
- Better aggregation performance