# Customer

## Purpose

The Customer table stores personal, contact, identity, financial, and risk-related information of bank customers. It acts as  the central entity of the banking system, with accounts, loans, credit cards, fixed deposits, beneficiaries, and nominees all associated with a customer.

---

## Primary Key

**customer_id**

Unique identifier for each customer.   

---

## Foreign Keys

**customer_segment_id** → customer_segment.customer_segment_id

Defines the category of the customer.

Examples:

- Retail
- Premium
- Corporate


**risk_category_id** → risk_category.risk_category_id

Represents the customer's risk profile.

Examples:

- Low Risk
- Medium Risk
- High Risk
- Very High Risk

---

## Relationships

Customer

├── Account (One-to-Many)

├── Loan (One-to-Many)

├── Credit Card (One-to-Many)

├── Fixed Deposit (One-to-Many)

├── Customer Beneficiary (One-to-Many)

└── Customer Nominee (One-to-Many)

A customer may own multiple banking products.

---

## Important Columns

### customer_code

Unique business identifier assigned to every customer.

---

### first_name

Customer's first name.

---

### last_name

Customer's last name.

---

### date_of_birth

Customer's date of birth.

---

### gender

Gender of the customer.

---

### email

Registered email address.

---

### phone_number

Registered mobile number.

---

### pan_number

Permanent Account Number (PAN).

Unique for every customer.

---

### aadhaar_number

Government-issued Aadhaar number.

Unique for every customer.

---

### occupation

Customer's profession or occupation.

---

### annual_income

Annual income of the customer in INR.

---

### credit_score

Customer's credit score.

Allowed range:

- 300 to 900

---

### city

City of residence.

---

### state

State of residence.

---

### customer_since

Date on which the customer joined the bank.

---

### customer_status

Current status of the customer.

Typical values:

- ACTIVE
- INACTIVE

---

## Business Rules

- Every customer has a unique customer code.
- PAN number must be unique.
- Aadhaar number must be unique.
- Email address must be unique.
- Phone number must be unique.
- Credit score must be between 300 and 900.
- Annual income cannot be negative.
- Every customer belongs to one customer segment.
- Every customer belongs to one risk category.
- A customer can own multiple accounts.
- A customer can have multiple loans.
- A customer can own multiple credit cards.
- A customer can have multiple fixed deposits.
- A customer can register multiple beneficiaries.
- A customer can register multiple nominees.

---

## Example Business Questions

- List all active customers.
- Find customers belonging to the Premium segment.
- Find customers with credit scores above 750.
- Show customers earning more than ₹20 lakhs annually.
- Find customers who joined after 2022.
- Count customers by city.
- Find customers having multiple accounts.
- Find customers who own both a loan and a credit card.
- Show customers grouped by risk category.
- List customers without any active accounts.