# Credit Card

## Purpose

The Credit Card table stores information about credit cards issued to bank customers. It maintains card details such as card type, credit limit, available limit, reward program, annual fee, cashback percentage, billing cycle, issue and expiry dates, and current card status.

Each credit card belongs to exactly one customer and is categorized under a specific card type.

---

## Primary Key

**card_id**

Unique identifier for each credit card.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the customer who owns the credit card.

**card_type_id** → card_type.card_type_id

Defines the category of the credit card.

Examples:

- Gold
- Platinum
- Silver
- Signature

---

## Relationships

Credit Card

├── customer (Many-to-One)

├── card_type (Many-to-One)

└── card_transaction (One-to-Many)

- Every credit card belongs to exactly one customer.
- Every credit card has one card type.
- One credit card can have multiple card transactions.

---

## Financial Attributes

### credit_limit

Maximum credit limit sanctioned for the card.

---

### available_limit

Remaining credit available for spending.

Should never exceed the credit limit.

---

### annual_fee

Annual maintenance fee charged for the card.

May be zero for lifetime-free cards.

---

### cashback_percentage

Cashback percentage applicable on eligible transactions.

---

## Card Attributes

### card_number

Unique card number assigned to the credit card.

---

### reward_program

Reward or loyalty program associated with the card.

Examples:

- Reward Points
- Cashback
- Travel Rewards
- Fuel Rewards
- Air Miles

---

### billing_cycle

Billing date of the credit card.

Typically represents the day of the month when the billing statement is generated.

Example:

- 5
- 10
- 15
- 20
- 25

---

### issue_date

Date on which the credit card was issued.

---

### expiry_date

Date on which the credit card expires.

A replacement card is typically issued before this date.

---

## Status Information

### card_status

Current status of the credit card.

Typical values:

- ACTIVE
- BLOCKED
- EXPIRED
- CLOSED

*(Update these values if your generated data uses different statuses.)*

---

## Business Rules

- Every credit card belongs to exactly one customer.
- Every credit card has one card type.
- Card number must be unique.
- Credit limit must always be greater than zero.
- Available limit cannot be negative.
- Available limit should never exceed the credit limit.
- Expiry date must always be after the issue date.
- Cashback percentage depends on the card type or reward program.
- One credit card can have multiple transactions.

---

## Example Business Questions

- List all active credit cards.
- Find customers with Platinum cards.
- Show cards expiring within the next six months.
- Find cards with credit limits above ₹10,00,000.
- Show average credit limit by card type.
- List customers having multiple credit cards.
- Find blocked credit cards.
- Show total available credit by customer.
- Find the top 10 customers by credit limit.
- Show cards grouped by reward program.