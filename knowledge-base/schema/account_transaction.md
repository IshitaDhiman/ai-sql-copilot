# Account Transaction

## Purpose

The Account Transaction table records every financial transaction performed on a bank account. It captures transaction details such as amount, transaction type, payment mode, category, merchant information, transaction status, and timestamp. This table forms the primary transaction ledger for customer accounts.

---

## Primary Key

**transaction_id**

Unique identifier for each account transaction.

---

## Foreign Keys

**account_id** → account.account_id

Identifies the bank account associated with the transaction.

**transaction_category_id** → transaction_category.transaction_category_id

Classifies the transaction into a business category.

Examples:

- Shopping
- Bills
- Food & Dining
- Travel
- Investment
- ATM Withdrawal

---

## Relationships

Account Transaction

├── account (Many-to-One)

└── transaction_category (Many-to-One)

- Every transaction belongs to exactly one account.
- Every transaction belongs to one transaction category.
- One account can have multiple transactions.

---

## Financial Attributes

### amount

Transaction amount.

Must always be greater than zero.

---

### currency

Currency in which the transaction was performed.

Default:

INR

---

## Transaction Attributes

### transaction_reference

Unique reference number generated for every transaction.

---

### transaction_type

Specifies whether money was credited or debited.

Possible values:

- CREDIT
- DEBIT

---

### payment_mode

Mode through which the transaction was performed.

Possible values:

- UPI
- NEFT
- RTGS
- IMPS
- CARD
- CASH
- CHEQUE

---

### transaction_category_id

Business classification of the transaction.

Used for reporting and analytics.

---

### merchant_name

Merchant or recipient associated with the transaction.

May be NULL for transactions such as cash deposits or internal transfers.

---

### remarks

Optional transaction description or remarks.

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

- Every transaction belongs to exactly one account.
- Every transaction has a unique transaction reference.
- Transaction amount must always be greater than zero.
- Every transaction has one transaction type.
- Every transaction has one payment mode.
- Every transaction has one transaction status.
- Every transaction belongs to one transaction category.
- Merchant name may be NULL depending on the transaction type.
- Transaction timestamp records the exact execution time.

---

## Example Business Questions

- Show all successful UPI transactions.
- Find transactions above ₹50,000.
- List failed transactions during the last 30 days.
- Calculate monthly transaction volume.
- Find total debit amount for a customer.
- Find total credit amount for an account.
- Show transactions by payment mode.
- Find the most frequently used transaction category.
- Show merchant-wise transaction totals.
- Find transactions performed today.
- Count successful and failed transactions by month.