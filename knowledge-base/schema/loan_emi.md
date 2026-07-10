# Loan EMI

## Purpose

The Loan EMI table stores the repayment schedule for customer loans. Each record represents a single Equated Monthly Installment (EMI), including its due date, payment amount, payment status, penalty, payment mode, delay information, and payment date.

---

## Primary Key

**emi_id**

Unique identifier for each EMI installment.

---

## Foreign Keys

**loan_id** → loan.loan_id

Identifies the loan to which the EMI belongs.

---

## Relationships

Loan EMI

└── loan (Many-to-One)

- Every EMI belongs to exactly one loan.
- A loan consists of multiple EMI installments.

---

## Financial Attributes

### amount

EMI amount payable for the installment.

Must always be greater than zero.

---

### penalty

Penalty charged due to delayed payment.

Default value:

0

---

## Payment Attributes

### installment_number

Sequence number of the EMI.

Examples:

- 1
- 2
- 3
- ...
- 120

---

### due_date

Scheduled due date of the EMI.

---

### paid_date

Date on which the EMI was paid.

Remains NULL if payment is pending.

---

### payment_mode

Mode used to pay the EMI.

Possible values:

- UPI
- NEFT
- RTGS
- IMPS
- CARD
- CASH
- CHEQUE

May be NULL until the EMI is paid.

---

### delay_days

Number of days payment was delayed.

Default:

0

---

## Status Information

### payment_status

Current payment status of the EMI.

Possible values:

- PAID
- PENDING
- OVERDUE

---

## Business Rules

- Every EMI belongs to exactly one loan.
- Installment numbers are sequential within a loan.
- EMI amount must always be greater than zero.
- Penalty defaults to zero for on-time payments.
- Delay days default to zero.
- Payment mode is recorded only after payment is made.
- Paid date remains NULL until the EMI is paid.
- One loan contains multiple EMI installments.

---

## Example Business Questions

- Show all overdue EMIs.
- Find EMIs due this month.
- List customers with pending EMIs.
- Calculate total penalty collected.
- Find customers with delayed EMI payments.
- Show monthly EMI collections.
- List loans that have all EMIs paid.
- Find the next EMI due for each customer.
- Calculate average delay in EMI payments.
- Show overdue EMIs branch-wise.