# Week 8 – E-Commerce Order Analytics System

## Celebal Technologies Internship

### Submitted By

**Name:** Gaurav Gaikwad

---

# Project Overview

The **E-Commerce Order Analytics System** is an end-to-end data engineering project developed using **Python, Pandas, SQLite, SQL, and Faker**.

The project simulates a real-world e-commerce environment by generating synthetic datasets, cleaning and validating data, storing the processed data in an SQLite database, performing SQL-based business analytics, generating reports, and validating the system using automated test cases.

This project demonstrates a complete ETL (Extract, Transform, Load) workflow and basic data engineering practices.

---

# Objective

The primary objectives of this project are:

- Generate realistic synthetic e-commerce datasets.
- Simulate real-world data quality issues.
- Perform data cleaning and preprocessing.
- Validate datasets using custom validation rules.
- Store cleaned data in an SQLite database.
- Perform SQL analytics to derive business insights.
- Build a Command Line Interface (CLI) reporting system.
- Implement automated test cases for data validation.

---

# Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Faker
- VS Code

---

# Project Structure

```
Week_8/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── cleaned/
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       ├── orders_clean.csv
│       └── order_items_clean.csv
│
├── database/
│   └── ecommerce.db
│
├── notebooks/
│   └── Week8_Project.ipynb
│
├── reports/
│   ├── issues_report.txt
│   └── sql_results.md
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── validate.py
│   ├── load_sqlite.py
│   ├── execute_queries.py
│   ├── cli_report.py
│   └── test_cases.py
│
├── sql/
│   └── queries.sql
│
├── README.md
└── requirements.txt
```

---

# Workflow

```
Generate Fake Data
        │
        ▼
Data Cleaning
        │
        ▼
Data Validation
        │
        ▼
SQLite Database
        │
        ▼
SQL Analytics
        │
        ▼
CLI Reporting
        │
        ▼
Testing
```

---

# Dataset Description

The project generates four synthetic datasets using the **Faker** library.

### Customers

Contains customer information including:

- Customer ID
- Customer Name
- Email
- Registration Date
- Customer Type

---

### Products

Contains product information including:

- Product ID
- Product Name
- Category
- Subcategory
- Cost Price

---

### Orders

Contains order information including:

- Order ID
- Customer ID
- Order Date
- Status
- Region

---

### Order Items

Contains transactional details including:

- Item ID
- Order ID
- Product ID
- Quantity
- Unit Price
- Discount Percentage

---

# Simulated Data Quality Issues

To simulate real-world datasets, intentional errors were introduced, including:

- Missing Customer IDs
- Invalid Email Addresses
- Invalid Date Formats
- Duplicate Records
- Inconsistent Product Names
- Negative Quantities

---

# Data Cleaning

The following preprocessing operations were performed:

- Removed duplicate records.
- Filled missing customer IDs.
- Standardized product names.
- Converted invalid dates.
- Corrected negative quantities.
- Standardized text formatting.

The cleaned datasets were stored in:

```
data/cleaned/
```

---

# Data Validation

Validation checks included:

- Invalid Email Detection
- Broken Foreign Key Detection
- Invalid Date Detection
- Missing Customer IDs
- Negative Quantity Detection

Validation results were stored in:

```
reports/issues_report.txt
```

---

# SQLite Database Integration

The cleaned datasets were successfully loaded into:

```
database/ecommerce.db
```

Database Tables:

- customers
- products
- orders
- order_items

---

# SQL Analytics

SQL queries were implemented to generate business insights such as:

- Revenue by Category
- Top Customers
- Monthly Order Summary
- Return Rate Analysis
- Top Selling Products
- Running Revenue Total
- Dense Ranking
- LAG Analysis
- Common Table Expressions (CTEs)
- NTILE Analysis
- Customer Statistics
- Product Contribution Analysis
- Self Join Analysis

The query outputs were saved in:

```
reports/sql_results.md
```

---

# Command Line Reporting

An interactive CLI application was developed to generate reports.

Available Reports:

- Daily Report
- Weekly Report
- Monthly Report

Each report displays:

- Total Orders
- Total Revenue
- Unique Customers
- Top Selling Products

---

# Automated Test Cases

The project includes automated validation tests for:

- Invalid Order IDs
- Negative Quantity
- Invalid Emails
- Missing Customer IDs
- Duplicate Product Names

These tests help verify data integrity after preprocessing.

---

# Output Files

Generated Outputs include:

- Raw CSV Files
- Cleaned CSV Files
- SQLite Database
- Validation Report
- SQL Result Report
- Interactive CLI Reports

---

# How to Run

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Generate Dataset

```bash
python scripts/generate_data.py
```

### Clean Data

```bash
python scripts/clean_data.py
```

### Validate Data

```bash
python scripts/validate.py
```

### Load SQLite Database

```bash
python scripts/load_sqlite.py
```

### Execute SQL Queries

```bash
python scripts/execute_queries.py
```

### Run CLI Report

```bash
python scripts/cli_report.py
```

### Execute Test Cases

```bash
python scripts/test_cases.py
```

---

# Key Learning Outcomes

Through this project, the following concepts were implemented:

- Synthetic Data Generation
- Data Cleaning
- Data Validation
- ETL Workflow
- SQLite Database Management
- SQL Analytics
- Command Line Reporting
- Automated Testing
- End-to-End Data Engineering Pipeline

---

# Conclusion

The **E-Commerce Order Analytics System** successfully demonstrates a complete end-to-end data engineering workflow using Python and SQLite.

The project covers synthetic data generation, preprocessing, validation, relational database integration, SQL-based analytics, reporting, and automated testing. It provides practical experience in building reliable data pipelines and applying data quality checks while generating meaningful business insights from transactional data.