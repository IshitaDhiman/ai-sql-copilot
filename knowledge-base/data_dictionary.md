# Data Dictionary

## Overview

The Data Dictionary defines business terminology used throughout the banking system. It provides clear definitions for common banking concepts, lookup values, statuses, and financial terms.

This document helps the AI SQL Copilot understand user intent and map natural language questions to the appropriate database schema.

---

# Customer

## Customer

An individual or organization that maintains one or more banking relationships with the bank.

A customer may own:

- Bank Accounts
- Loans
- Credit Cards
- Fixed Deposits
- Beneficiaries
- Nominees

---

## Customer Segment

Represents the category of a customer based on their banking relationship.

Examples:

- Standard
- Premium
- Corporate
- HNI (High Net Worth Individual)

---

## Risk Category

Represents the customer's lending or financial risk profile.

Examples:

- Low Risk
- Medium Risk
- High Risk

Used during loan approval and credit assessment.

---

## Credit Score

Numeric indicator of a customer's creditworthiness.

Typical Range:

300 – 900

Higher scores generally indicate lower lending risk.

---

# Banking

## Branch

Physical banking location where customer accounts and banking products are managed.

Each branch belongs to one bank.

---

## Employee

Bank staff responsible for customer servicing and banking operations.

Employees belong to departments and branches.

---

## Department

Organizational unit within the bank.

Examples:

- Operations
- Loans
- Customer Service
- IT
- Finance
- HR

---

# Account

## Bank Account

Financial account maintained by a customer.

Every account belongs to exactly one customer.

---

## Account Type

Defines the purpose of the account.

Examples:

- Savings
- Current
- Salary
- Fixed Deposit

---

## Account Balance

Current total balance available in the account.

---

## Available Balance

Amount immediately available for withdrawal or spending.

May differ from the account balance due to holds or pending transactions.

---

## Minimum Balance

Minimum amount required to be maintained in an account.

Applicable depending on account type.

---

## Interest Rate

Annual percentage rate used to calculate interest earned or charged.

Applicable to products such as:

- Savings Accounts
- Fixed Deposits
- Loans

---

# Transactions

## Transaction

Movement of money into or out of an account.

---

## Transaction Type

Defines the direction of money movement.

Values:

- CREDIT
- DEBIT

---

## Payment Mode

Method used to perform a financial transaction.

Values:

- UPI
- NEFT
- RTGS
- IMPS
- CARD
- CASH
- CHEQUE

---

## Transaction Category

Business classification of a transaction.

Examples:

- Shopping
- Groceries
- Bills
- Travel
- Fuel
- Entertainment
- Investment

---

## Transaction Status

Represents the processing outcome of a transaction.

Values:

- SUCCESS
- FAILED
- PENDING

---

## Transaction Reference

Unique identifier assigned to every financial transaction.

Used for tracking and reconciliation.

---

# Loans

## Loan

Amount borrowed from the bank under agreed repayment terms.

---

## Loan Type

Category of loan issued by the bank.

Examples:

- Home Loan
- Personal Loan
- Car Loan
- Education Loan
- Business Loan
- Gold Loan

---

## Sanctioned Amount

Loan amount approved by the bank.

---

## Disbursed Amount

Actual amount released to the borrower.

---

## Outstanding Amount

Remaining unpaid loan balance.

---

## EMI (Equated Monthly Installment)

Fixed monthly payment made by the customer towards loan repayment.

Consists of:

- Principal Component
- Interest Component

---

## Processing Fee

One-time fee charged during loan processing.

---

## Collateral

Asset pledged as security against a loan.

Examples:

- Property
- Gold
- Vehicle
- Fixed Deposit

---

## Loan Status

Represents the current state of a loan.

Typical values:

- ACTIVE
- CLOSED
- DEFAULTED
- WRITTEN_OFF

---

# Loan EMI

## Installment Number

Sequential number assigned to each EMI.

Example:

Loan with 60-month tenure contains installments:

1 → 60

---

## Penalty

Additional charge applied for delayed EMI payments.

---

## Delay Days

Number of days by which an EMI payment was delayed.

---

## EMI Payment Status

Represents the repayment status of an EMI.

Values:

- PAID
- PENDING
- OVERDUE

---

# Fixed Deposit

## Fixed Deposit (FD)

Investment product where money is deposited for a fixed tenure to earn interest.

---

## Principal Amount

Initial amount invested.

---

## Maturity Amount

Amount receivable upon maturity.

Includes:

- Principal
- Interest Earned

---

## Tenure

Duration of the investment.

Measured in months.

---

## Interest Payout

Specifies when interest is paid.

Examples:

- Monthly
- Quarterly
- Half-Yearly
- Annually
- At Maturity

---

## Fixed Deposit Status

Represents the lifecycle of an FD.

Typical values:

- ACTIVE
- MATURED
- CLOSED
- PREMATURE_CLOSED

---

# Credit Cards

## Credit Card

Bank-issued payment card allowing customers to borrow up to an approved credit limit.

---

## Card Type

Defines the category of the credit card.

Examples:

- Classic
- Gold
- Platinum
- Titanium
- Signature

---

## Credit Limit

Maximum borrowing limit approved for a card.

---

## Available Limit

Remaining amount available for spending.

---

## Reward Program

Benefits associated with card usage.

Examples:

- Cashback
- Reward Points
- Travel Rewards
- Fuel Rewards
- Air Miles

---

## Cashback

Percentage of transaction amount returned to the customer.

---

## Billing Cycle

Day of the month when the credit card statement is generated.

---

## Card Status

Represents the current state of a credit card.

Typical values:

- ACTIVE
- BLOCKED
- EXPIRED
- CLOSED

---

# Card Transactions

## Merchant

Business where the card transaction occurred.

Examples:

- Amazon
- Flipkart
- Swiggy
- Reliance Fresh

---

## Cashback Earned

Cashback credited for a particular card transaction.

---

# Beneficiaries

## Beneficiary

Recipient registered by a customer for fund transfers.

---

## IFSC Code

Indian Financial System Code.

Uniquely identifies a bank branch for electronic fund transfers.

---

## Nickname

Optional alias assigned by the customer for easy beneficiary identification.

---

# Nominees

## Nominee

Person authorized to receive banking assets in the event of the customer's death.

---

## Relationship

Relationship between the customer and the nominee.

Examples:

- Father
- Mother
- Spouse
- Son
- Daughter
- Brother
- Sister
- Guardian

---

# Financial Terms

## Principal

Original amount invested or borrowed.

---

## Interest

Amount earned on deposits or charged on loans.

---

## Annual Percentage Rate (APR)

Annualized interest rate applied to loans or credit products.

---

## Currency

Monetary unit used for financial transactions.

Default:

INR (Indian Rupee)

---

## Merchant City

City where the merchant is located.

---

## Merchant Country

Country where the merchant is located.

Useful for identifying international transactions.