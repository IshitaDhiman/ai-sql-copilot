# Employee

## Purpose

The Employee table stores information about all bank employees. It contains personal details, job-related information, department assignment, branch assignment, reporting hierarchy, salary, performance rating, and employment status. Employees are responsible for customer service, branch operations, loan processing, and other banking activities.

---

## Primary Key

**employee_id**

Unique identifier for each employee.

---

## Foreign Keys

**branch_id** → branch.branch_id

Each employee is assigned to one bank branch.

**department_id** → employee_department.department_id

Defines the department in which the employee works.

**manager_id** → employee.employee_id (Self Reference)

Represents the reporting manager of the employee. Senior managers or branch heads may not have a reporting manager.

---

## Relationships

Employee

├── Branch (Many-to-One)

├── Employee Department (Many-to-One)

└── Employee (Self Relationship)

- A branch can have multiple employees.
- A department can have multiple employees.
- Every employee belongs to one branch.
- Every employee belongs to one department.
- A manager can supervise multiple employees.

---

## Important Columns

### employee_code

Unique employee identifier used within the bank.

---

### first_name

Employee's first name.

---

### last_name

Employee's last name.

---

### email

Official employee email address.

---

### phone_number

Employee contact number.

---

### designation

Employee's job title within the bank.

Examples:

- Branch Manager
- Relationship Manager
- Cashier
- Loan Officer
- Operations Executive

---

### salary

Employee's monthly or annual salary depending on the organization's payroll policy.

---

### performance_rating

Performance rating assigned during employee evaluation.

Allowed range:

- 0.00 to 5.00

---

### hire_date

Date on which the employee joined the organization.

---

### status

Current employment status.

Typical values:

- ACTIVE
- INACTIVE
- RESIGNED

---

## Business Rules

- Every employee belongs to exactly one branch.
- Every employee belongs to exactly one department.
- Employee code must be unique.
- Email address must be unique.
- Salary must always be greater than zero.
- Performance rating must be between 0 and 5.
- A manager can supervise multiple employees.
- Senior managers may have a NULL `manager_id`.
- Employees cannot report to themselves.

---

## Example Business Questions

- List all employees working in a specific branch.
- Find employees belonging to a particular department.
- Count employees in each branch.
- Find the reporting manager of an employee.
- List all employees under a specific manager.
- Find employees with performance ratings above 4.
- Show the average salary by department.
- Find employees hired during the last year.
- List all active employees.