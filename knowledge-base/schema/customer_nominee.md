# Customer Nominee

## Purpose

The Customer Nominee table stores nominee information provided by customers for their banking relationship. A nominee is the person authorized to receive the customer's banking assets in the event of the customer's death, subject to applicable banking regulations.

Each nominee belongs to exactly one customer. A customer may register one or more nominees depending on the banking product and applicable policies.

---

## Primary Key

**nominee_id**

Unique identifier for each nominee.

---

## Foreign Keys

**customer_id** → customer.customer_id

Identifies the customer who registered the nominee.

---

## Relationships

Customer Nominee

└── customer (Many-to-One)

- Every nominee belongs to exactly one customer.
- One customer can register multiple nominees.

---

## Nominee Attributes

### nominee_name

Full name of the nominee.

---

### relationship

Relationship between the customer and the nominee.

Examples:

- Father
- Mother
- Spouse
- Son
- Daughter
- Brother
- Sister
- Friend
- Guardian

---

### date_of_birth

Date of birth of the nominee.

May be NULL.

---

### phone_number

Contact number of the nominee.

May be NULL.

---

## Business Rules

- Every nominee belongs to exactly one customer.
- A customer can register multiple nominees.
- Nominee name is mandatory.
- Relationship with the customer is mandatory.
- Date of birth is optional.
- Phone number is optional.
- Nominee information is maintained for banking products requiring nomination facilities.

---

## Example Business Questions

- List nominees registered by a customer.
- Find customers without any nominees.
- Count nominees by relationship.
- List all spouse nominees.
- Show nominees added for customers in a particular city.
- Find nominees whose date of birth is available.
- Show customers having multiple nominees.
- Count nominees registered across all customers.
- Find nominees with missing phone numbers.
- Show relationship-wise nominee distribution.