# Business Rules

## Overview

This document defines business rules governing the banking system. These rules describe relationships, constraints, and business logic that extend beyond database constraints.

The AI SQL Copilot uses these rules to better understand the banking domain and generate logically correct SQL queries.

---

# Customer Rules

- Every customer is uniquely identified by `customer_id`.
- Every customer has a unique customer code.
- Every customer belongs to exactly one customer segment.
- Every customer belongs to exactly one risk category.
- Every customer may own multiple bank accounts.
- Every customer may have multiple loans.
- Every customer may own multiple credit cards.
- Every customer may create multiple fixed deposits.
- Every customer may register multiple beneficiaries.
- Every customer may register multiple nominees.
- Customer PAN number must be unique.
- Customer Aadhaar number must be unique.
- Customer email address must be unique.
- Customer phone number must be unique.
- Credit score ranges from 300 to 900.
- Annual income cannot be negative.

---

# Branch Rules

- Every branch belongs to one bank.
- Every account is opened under one branch.
- Every loan is processed through one branch.
- Every employee belongs to one branch.
- A branch can manage thousands of customers.
- A branch can manage multiple employees.
- A branch can issue multiple loans.

---

# Employee Rules

- Every employee belongs to one department.
- Every employee works in one branch.
- Every employee has a unique employee code.
- Every employee may report to one manager.
- Branch managers may supervise multiple employees.
- Employee performance rating ranges from 0 to 5.
- Employee salary must always be greater than zero.

---

# Account Rules

- Every account belongs to exactly one customer.
- Every account belongs to one branch.
- Every account has one account type.
- Account numbers are unique.
- Account balance cannot be negative.
- Available balance cannot be negative.
- Available balance should never exceed account balance.
- Minimum balance depends on the account type.
- Savings accounts may earn interest.
- Current accounts typically do not earn interest.
- One customer may own multiple accounts.

---

# Account Transaction Rules

- Every transaction belongs to exactly one account.
- Every transaction has one transaction type.
- Every transaction has one payment mode.
- Every transaction belongs to one transaction category.
- Every transaction has one transaction status.
- Transaction reference numbers are unique.
- Transaction amount must always be greater than zero.
- Debit transactions reduce available balance.
- Credit transactions increase available balance.
- Failed transactions should not affect account balance.
- Pending transactions may temporarily reserve funds.

---

# Loan Rules

- Every loan belongs to exactly one customer.
- Every loan is issued through one branch.
- Every loan belongs to one loan type.
- One customer may have multiple loans.
- Outstanding amount cannot exceed disbursed amount.
- Disbursed amount cannot exceed sanctioned amount.
- EMI amount depends on loan amount, interest rate, and tenure.
- Processing fee is charged once during loan creation.
- Closure date is recorded only after complete repayment.

---

# Loan EMI Rules

- Every EMI belongs to exactly one loan.
- One loan consists of multiple EMI installments.
- Installment numbers are sequential.
- EMI amount must always be greater than zero.
- Delay days default to zero.
- Penalty defaults to zero.
- Payment mode is recorded after payment.
- Paid date remains NULL until payment.
- Overdue EMIs may attract penalties.

---

# Fixed Deposit Rules

- Every fixed deposit belongs to one customer.
- One customer may create multiple fixed deposits.
- Principal amount must always be greater than zero.
- Maturity amount should be greater than principal amount.
- Maturity date depends on start date and tenure.
- Interest rate depends on tenure and bank policy.
- Premature closure may reduce interest earned.

---

# Credit Card Rules

- Every credit card belongs to exactly one customer.
- Every credit card has one card type.
- Card numbers are unique.
- Credit limit must always be greater than zero.
- Available limit cannot exceed credit limit.
- Available limit decreases after purchases.
- Available limit increases after bill payment.
- Expiry date must always be after issue date.
- Cashback depends on reward program.
- One customer may own multiple credit cards.

---

# Card Transaction Rules

- Every card transaction belongs to one credit card.
- Every transaction belongs to one transaction category.
- Transaction amount must always be greater than zero.
- Cashback cannot be negative.
- Successful transactions reduce available credit limit.
- Failed transactions should not reduce available credit.
- Cashback depends on card benefits.
- Merchant information should be stored whenever available.

---

# Beneficiary Rules

- Every beneficiary belongs to one customer.
- Every beneficiary belongs to one bank.
- A customer may register multiple beneficiaries.
- Nickname is optional.
- Beneficiary account number is mandatory.
- IFSC code identifies the beneficiary branch.

---

# Nominee Rules

- Every nominee belongs to one customer.
- A customer may register multiple nominees.
- Nominee name is mandatory.
- Relationship is mandatory.
- Phone number is optional.
- Date of birth is optional.

---

# Banking Rules

- Customers may simultaneously own accounts, loans, credit cards, and fixed deposits.
- Customers are not required to own every banking product.
- Loan repayment history affects customer creditworthiness.
- Banking products remain linked to the owning customer throughout their lifecycle.
- Financial reports should consider only successful transactions unless specified otherwise.
- Active products are generally included in operational reporting.
- Closed or inactive products may still appear in historical reports.