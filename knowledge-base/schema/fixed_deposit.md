# Fixed Deposit

## Purpose

The Fixed Deposit table stores information about customers' fixed deposit (FD) investments. It records the principal amount, applicable interest rate, tenure, maturity amount, interest payout option, maturity date, and current status of each fixed deposit.

Each fixed deposit belongs to one customer and represents a time-bound investment that earns interest over a predefined period.

---

## Primary Key

**fd_id**

Unique identifier for each fixed deposit.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the customer who owns the fixed deposit.

---

## Relationships

Fixed Deposit

└── customer (Many-to-One)

- Every fixed deposit belongs to exactly one customer.
- A customer can own multiple fixed deposits.

---

## Financial Attributes

### principal_amount

Initial amount invested by the customer.

Must always be greater than zero.

---

### interest_rate

Annual interest rate applicable to the fixed deposit.

---

### tenure_months

Duration of the fixed deposit in months.

Examples:

- 6
- 12
- 24
- 36
- 60
- 120

---

### maturity_amount

Total amount payable to the customer upon maturity.

Includes principal and earned interest.

---

## Deposit Attributes

### interest_payout

Specifies how interest is paid to the customer.

Typical values:

- MONTHLY
- QUARTERLY
- HALF_YEARLY
- ANNUALLY
- MATURITY

*(Update these if your generated values differ.)*

---

### start_date

Date on which the fixed deposit was created.

---

### maturity_date

Date on which the fixed deposit reaches maturity.

---

## Status Information

### status

Current status of the fixed deposit.

Typical values:

- ACTIVE
- MATURED
- CLOSED
- PREMATURE_CLOSED

*(Update according to the values used in your generated data.)*

---

## Business Rules

- Every fixed deposit belongs to exactly one customer.
- Principal amount must always be greater than zero.
- Maturity amount should be greater than or equal to the principal amount.
- Maturity date is calculated using the start date and tenure.
- Interest rate depends on the FD tenure and bank policy.
- A customer can own multiple fixed deposits.
- Interest payout determines when interest is credited.
- Closed fixed deposits cannot receive further interest.

---

## Example Business Questions

- List all active fixed deposits.
- Find fixed deposits maturing this month.
- Calculate total fixed deposit investment by customer.
- Show total fixed deposits branch-wise (through customer accounts if applicable).
- Find customers with more than one fixed deposit.
- Show the average fixed deposit amount.
- Find the highest-value fixed deposits.
- Calculate expected maturity amount for all active fixed deposits.
- List prematurely closed fixed deposits.
- Show total fixed deposit portfolio by interest rate.