# Card Transaction

## Purpose

The Card Transaction table records every transaction performed using a credit card. It stores details such as transaction amount, merchant information, cashback earned, transaction category, transaction status, and transaction timestamp.

Each transaction belongs to exactly one credit card and is categorized under a business transaction category.

---

## Primary Key

**card_transaction_id**

Unique identifier for each card transaction.

---

## Foreign Keys

**card_id** → credit_card.card_id

Identifies the credit card used for the transaction.

**transaction_category_id** → transaction_category.transaction_category_id

Classifies the transaction into a business category.

Examples:

- Shopping
- Food & Dining
- Travel
- Entertainment
- Fuel
- Utilities
- Healthcare
- Groceries

---

## Relationships

Card Transaction

├── credit_card (Many-to-One)

└── transaction_category (Many-to-One)

- Every card transaction belongs to exactly one credit card.
- Every transaction belongs to one transaction category.
- One credit card can have multiple transactions.

---

## Financial Attributes

### amount

Amount spent in the transaction.

Must always be greater than zero.

---

### cashback_earned

Cashback credited for the transaction.

Defaults to zero if no cashback is applicable.

---

## Transaction Attributes

### transaction_reference

Unique reference generated for every card transaction.

---

### merchant_name

Name of the merchant where the transaction occurred.

Examples:

- Amazon
- Flipkart
- Swiggy
- Zomato
- Reliance Fresh

---

### merchant_city

City where the merchant is located.

May be NULL for online transactions.

---

### merchant_country

Country where the merchant is located.

May be NULL for domestic online transactions.

---

### transaction_timestamp

Date and time when the transaction occurred.

---

## Status Information

### transaction_status

Current processing status of the transaction.

Possible values:

- SUCCESS
- FAILED
- PENDING

---

## Business Rules

- Every transaction belongs to exactly one credit card.
- Every transaction belongs to one transaction category.
- Transaction reference must be unique.
- Transaction amount must always be greater than zero.
- Cashback earned cannot be negative.
- Cashback depends on the card's reward program and cashback percentage.
- Merchant information should be recorded whenever available.
- One credit card can have multiple transactions.

---

## Example Business Questions

- Show all successful card transactions.
- Find transactions above ₹25,000.
- Calculate total card spending by customer.
- Show monthly card spending.
- Find the highest spending merchants.
- Calculate cashback earned by customer.
- Show spending by transaction category.
- Find failed card transactions.
- List international card transactions.
- Show top 10 customers by card spending.