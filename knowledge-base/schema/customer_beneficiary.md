# Customer Beneficiary

## Purpose

The Customer Beneficiary table stores beneficiary accounts registered by customers for fund transfers. It maintains beneficiary details such as beneficiary name, bank, account number, IFSC code, nickname, and registration date.

Each beneficiary belongs to one customer and is associated with one bank.

---

## Primary Key

**beneficiary_id**

Unique identifier for each beneficiary.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the customer who added the beneficiary.

**bank_id** → bank.bank_id

Identifies the beneficiary's bank.

---

## Relationships

Customer Beneficiary

├── customer (Many-to-One)

└── bank (Many-to-One)

- Every beneficiary belongs to exactly one customer.
- Every beneficiary belongs to one bank.
- One customer can register multiple beneficiaries.

---

## Beneficiary Attributes

### beneficiary_name

Name of the beneficiary account holder.

---

### account_number

Bank account number of the beneficiary.

---

### ifsc_code

IFSC code of the beneficiary's bank branch.

Used for NEFT, RTGS, and IMPS transfers.

---

### nickname

Optional nickname assigned by the customer for easy identification.

Examples:

- Mom
- Rent
- Office Account
- Savings
- Friend

May be NULL.

---

### added_date

Date on which the beneficiary was registered.

---

## Business Rules

- Every beneficiary belongs to exactly one customer.
- Every beneficiary is associated with one bank.
- A customer can register multiple beneficiaries.
- Multiple customers may register the same beneficiary account.
- Nickname is optional.
- IFSC code identifies the beneficiary branch.
- Beneficiary details are required before initiating most bank transfers.

---

## Example Business Questions

- List all beneficiaries of a customer.
- Count beneficiaries registered by each customer.
- Find beneficiaries added this month.
- Show beneficiaries grouped by bank.
- Find customers having more than five beneficiaries.
- List beneficiaries belonging to a specific bank.
- Show customers who have not registered any beneficiaries.
- Find the most commonly used beneficiary banks.
- List beneficiaries with nicknames.
- Show recently added beneficiaries.