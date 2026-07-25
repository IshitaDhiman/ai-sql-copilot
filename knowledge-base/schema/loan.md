# Loan

## Purpose

The Loan table stores information about loans sanctioned to customers. It maintains loan details such as loan type, sanctioned amount, disbursed amount, outstanding balance, interest rate, tenure, EMI, processing fee, collateral information, approval date, and loan status. Each loan belongs to one customer and is processed through one bank branch.

---

## Primary Key

**loan_id**

Unique identifier for each loan.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the customer who owns the loan.

**branch_id** → branch.branch_id

Identifies the branch that processed the loan.

**loan_type_id** → loan_type.loan_type_id

Defines the category of the loan.

Examples:

- Home Loan
- Personal Loan
- Car Loan
- Education Loan
- Gold Loan

---

## Relationships

Loan

├── customer (Many-to-One)

├── branch (Many-to-One)

├── loan_type (Many-to-One)

└── loan_emi (One-to-Many)

- Every loan belongs to exactly one customer.
- Every loan is issued by one branch.
- Every loan belongs to one loan type.
- One loan can have multiple EMI installments.

---

## Financial Attributes

### sanctioned_amount

Total loan amount approved by the bank.

---

### disbursed_amount

Actual amount released to the customer.

---

### outstanding_amount

Remaining unpaid loan balance.

---

### interest_rate

Annual interest rate applicable to the loan.

---

### tenure_months

Loan repayment duration in months.

Examples:

- 12
- 24
- 36
- 60
- 120
- 240
- 360

---

### emi_amount

Fixed monthly installment payable by the customer.

---

### processing_fee

One-time fee charged during loan processing.

---

## Loan Attributes

### collateral_type

Asset pledged against the loan, if applicable.

Examples:

- Property
- Vehicle
- Gold
- Fixed Deposit

May be NULL for unsecured loans.

---

### approval_date

Date on which the loan was approved.

---

### closure_date

Date on which the loan was fully repaid.

Remains NULL for active loans.

---

## Status Information

### loan_status

Current status of the loan.

Typical values:

- ACTIVE
- CLOSED
- DEFAULTED
- WRITTEN_OFF

*(Update this list if your lookup values are different.)*

---

## Business Rules

- Every loan belongs to exactly one customer.
- Every loan is associated with one branch.
- Every loan has one loan type.
- Outstanding amount cannot exceed disbursed amount.
- Disbursed amount cannot exceed sanctioned amount.
- EMI amount should be calculated using loan amount, interest rate, and tenure.
- Processing fee is charged once during loan issuance.
- Closure date is populated only after the loan is fully repaid.
- One loan consists of multiple EMI installments.

---

## Example Business Questions

- List all active loans.
- Find customers with home loans above ₹50 lakhs.
- Show total outstanding loan amount by branch.
- Find customers having multiple loans.
- Calculate average loan amount by loan type.
- Show loans approved during the current year.
- Find loans that have been fully closed.
- Find customers with overdue loan repayments.
- Show branch-wise loan portfolio.
- List the top 10 largest active loans.