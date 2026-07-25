# Knowledge Base

## Overview

The Knowledge Base serves as the domain knowledge repository for the AI SQL Copilot. It contains structured documentation about the banking database schema, business rules, terminology, and example business questions.

Instead of relying solely on SQL table definitions, the AI retrieves relevant documentation from this knowledge base to better understand the banking domain before generating SQL queries.

This enables more accurate, context-aware, and business-friendly SQL generation using Retrieval-Augmented Generation (RAG).

---

## Directory Structure

```
knowledge-base/
│
├── README.md
├── schema/
│   ├── branch.md
│   ├── employee.md
│   ├── customer.md
│   ├── account.md
│   ├── account_transaction.md
│   ├── loan.md
│   ├── loan_emi.md
│   ├── fixed_deposit.md
│   ├── credit_card.md
│   ├── card_transaction.md
│   ├── customer_beneficiary.md
│   └── customer_nominee.md
│
├── business_rules.md
├── data_dictionary.md
└── sample_queries.md
```

---

# Components

## 1. Schema Documentation

Each table is documented individually to describe:

- Table purpose
- Primary key
- Foreign keys
- Relationships
- Financial attributes
- Business attributes
- Status information
- Business rules
- Example business questions

This documentation helps the AI understand both the database structure and the business meaning of each table.

---

## 2. Business Rules

Contains cross-table business logic that may not be enforced by database constraints.

Examples include:

- A customer may own multiple accounts.
- An account belongs to exactly one customer.
- Outstanding loan amount cannot exceed disbursed amount.
- Available balance should not exceed account balance.

These rules help the AI generate logically correct SQL.

---

## 3. Data Dictionary

Provides business definitions for commonly used banking terms such as:

- Customer Segment
- Risk Category
- Credit Score
- Loan Status
- Payment Mode
- Transaction Status

This improves the AI's understanding of business terminology.

---

## 4. Sample Queries

Contains realistic banking questions that users may ask.

Examples include:

- Find customers with multiple accounts.
- Show branch-wise deposits.
- List overdue EMIs.
- Show top customers by account balance.

These examples improve retrieval quality during SQL generation.

---

# How the AI Uses This Knowledge Base

The AI SQL Copilot follows a Retrieval-Augmented Generation (RAG) workflow.

```
User Question
       │
       ▼
Embedding Model
       │
       ▼
Vector Search
       │
       ▼
Relevant Knowledge Base Documents
       │
       ▼
Large Language Model (LLM)
       │
       ▼
Generated SQL Query
       │
       ▼
SQL Validation
       │
       ▼
Database Execution
```

Only the most relevant documentation is retrieved for each question, reducing prompt size while improving SQL accuracy.

---

# Design Principles

- One Markdown document per database table.
- Documentation mirrors the actual PostgreSQL schema.
- Business context is documented alongside technical details.
- Relationships are explicitly described.
- Example business questions are included for retrieval optimization.
- Documentation is modular and easy to maintain.

---

# Future Enhancements

- Automatic documentation generation from PostgreSQL metadata.
- Semantic search using embeddings.
- Vector storage using pgvector.
- Business glossary expansion.
- Few-shot SQL examples for improved AI performance.
- Automatic synchronization with schema changes.

---

# Purpose

This Knowledge Base forms the foundation of the AI SQL Copilot by combining database metadata with business knowledge, enabling accurate and context-aware SQL generation for banking use cases.