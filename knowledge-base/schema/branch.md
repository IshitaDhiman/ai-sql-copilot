# Branch

## Purpose

The Branch table stores information about every bank branch. It represents the physical locations where banking services are provided. Customer accounts, employees, and loans are associated with a branch.

---

## Primary Key

**branch_id**

Unique identifier for each branch.

---

## Foreign Keys

This table does not contain any foreign keys.

---

## Relationships

Branch
├── Employee (One-to-Many)
├── Account (One-to-Many)
└── Loan (One-to-Many)

A single branch can have many employees, accounts, and loans.

---

## Important Columns

### branch_code

Unique code used to identify a branch.

### branch_name

Official name of the branch.

### city

City where the branch is located.

### state

State where the branch is located.

### ifsc_code

Unique IFSC code used for electronic fund transfers.

### phone_number

Branch contact number.

### email

Official branch email address.

### opened_date

Date on which the branch started operations.

### branch_status

Current operational status of the branch.

Typical values:

- ACTIVE
- INACTIVE

---

## Business Rules

- Every branch has a unique branch code.
- Every branch has a unique IFSC code.
- Every employee belongs to exactly one branch.
- Every account is opened under one branch.
- Every loan is processed through one branch.
- Branch information is shared across multiple banking products.

---

## Example Business Questions

- List all active branches.
- Count customers served by each branch.
- Find total deposits branch-wise.
- Find branches with the highest number of loans.
- Show branches with no active employees.