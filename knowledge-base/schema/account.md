# Account

## Purpose

The Account table stores information about all customer bank accounts. It maintains account details such as account number, account type, balances, interest rate, branch, and account status. Every account belongs to exactly one customer and is opened under one bank branch.

---

## Primary Key

**account_id**

Unique identifier for each bank account.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the owner of the account.

**branch_id** → branch.branch_id

Identifies the branch where the account was opened.

**account_type_id** → account_type.account_type_id

Defines the type of account.

Examples:

- Savings Account
- Current Account
- Salary Account
- Fixed Deposit Account (if applicable)

---

## Relationships

Account

├── customer (Many-to-One)

├── branch (Many-to-One)

├── account_type (Many-to-One)

└── account_transaction (One-to-Many)

Each account belongs to one customer.

Each account belongs to one branch.

Each account has one account type.

One account can have multiple transactions.

---

## Important Columns

### account_number

Unique account number assigned by the bank.

---

### balance

Current balance maintained in the account.

Must be greater than or equal to zero.

---

### available_balance

Amount currently available for withdrawal or spending.

Must be greater than or equal to zero.

---

### minimum_balance

Minimum balance required to maintain the account.

---

### interest_rate

Interest rate applicable to the account.

Applicable primarily to interest-bearing accounts such as Savings Accounts.

---

### currency

Currency in which the account is maintained.

Default:

INR

---

### opened_date

Date on which the account was opened.

---

### account_status

Current status of the account.

Typical values:

- ACTIVE
- INACTIVE
- BLOCKED
- CLOSED

---

## Business Rules

- Every account has a unique account number.
- Every account belongs to exactly one customer.
- Every account is associated with exactly one branch.
- Every account has one account type.
- Balance cannot be negative.
- Available balance cannot be negative.
- Available balance should not exceed the total account balance.
- Minimum balance depends on the account type.
- Interest rate is applicable only for eligible account types.
- One account can have multiple transactions.

---

## Example Business Questions

- List all active accounts.
- Find accounts with balances greater than ₹10,00,000.
- Show total deposits by branch.
- Find customers having multiple accounts.
- List inactive accounts.
- Find average account balance by account type.
- Show accounts opened during the current year.
- Find customers whose available balance is below the minimum balance.
- Count accounts by account type.
- Find the top 10 accounts by balance.