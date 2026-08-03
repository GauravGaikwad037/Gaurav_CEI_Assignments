# 🛍️ Week 1 – Shopping Dataset Exploration & Data Cleaning using Pandas

## 📌 Objective

The objective of this assignment is to understand the fundamentals of Python and Pandas by performing data loading, exploration, preprocessing, and cleaning operations on multiple shopping dataset CSV files. The assignment demonstrates practical data manipulation skills that are essential for data analysis and machine learning workflows.

---

## 🚀 Technologies Used

* Python 3.13
* Pandas
* OS Module
* Jupyter Notebook
* Visual Studio Code

---

## 📂 Project Structure

```
Week_1/
│
├── data/
│   ├── raw/
│   │   ├── *.csv
│   │   └── (Shopping Dataset Files)
│   │
│   └── cleaned/
│       └── cleaned_shopping_dataset.csv
│
├── week1.ipynb
└── README.md
```

---

## 📊 Tasks Performed

### ✅ Data Loading

* Loaded all shopping dataset CSV files from the `data/raw` directory.
* Combined multiple datasets into a single Pandas DataFrame for unified analysis.

### ✅ Data Exploration

Performed exploratory analysis using:

* `head()`
* `tail()`
* `shape`
* `columns`
* `dtypes`

to understand the dataset structure and contents.

### ✅ Missing Value Handling

* Identified missing values across all columns.
* Filled missing categorical values with `"Unknown"`.
* Filled missing numerical values with `0`.

### ✅ Data Cleaning

* Removed duplicate records.
* Improved dataset consistency for further analysis.

### ✅ Basic Data Operations

* Selected important columns for inspection.
* Filtered products based on rating conditions.

### ✅ Feature Engineering

Created new columns:

* `quantity`
* `total_amount = final_price × quantity`

to demonstrate derived feature creation.

### ✅ Export

Saved the cleaned and processed dataset as:

```
data/cleaned/cleaned_shopping_dataset.csv
```

---

## 📈 Outcome

Successfully performed end-to-end preprocessing and cleaning of multiple shopping datasets using Pandas, including:

* Data loading
* Data exploration
* Missing value handling
* Duplicate removal
* Row filtering
* Column selection
* Derived feature creation
* Cleaned dataset export

---

## 💡 Key Learning

Through this assignment, I gained hands-on experience in:

* Working with multiple CSV files
* Using Pandas for real-world data manipulation
* Data preprocessing techniques
* Feature engineering
* Preparing datasets for downstream analytics and machine learning tasks

---

# Week 2 - SQL Based Data Analysis

## Objective

Analyze sales data using SQL with filtering, aggregation, joins, sorting, grouping, and business queries.

## Technologies Used

* SQLite
* SQL
* Python
* Pandas
* Jupyter Notebook
* VS Code

## Tasks Performed

* Created relational database
* Created customers, products, orders, and order_items tables
* Inserted sample records
* Applied WHERE filtering
* Used GROUP BY aggregations
* Performed sorting and limiting
* Executed JOIN operations
* Analyzed monthly sales trends
* Validated data quality
* Generated business insights

## Files Included

* ecommerce_sales_database.ipynb
* sql_queries.sql
* ecommerce.db
* README.md

🚀 Week 3 - SQL-Based Data Analysis Using Subqueries, CTEs & Window Functions
📌 Overview

This project is a part of my Celebal Technologies Internship 2026. The objective of this assignment is to perform advanced SQL-based data analysis on the Superstore dataset using Subqueries, Common Table Expressions (CTEs), and Window Functions to solve real-world business problems and generate meaningful insights.

🎯 Objective
Load the Superstore dataset into a SQL database.
Create normalized database tables.
Perform advanced SQL analysis using:
Subqueries
Common Table Expressions (CTEs)
Window Functions
Solve business-oriented SQL problems.
Generate meaningful insights from sales data.
🛠️ Technologies Used
Python 3.13
SQLite
SQL
Pandas
Jupyter Notebook
VS Code
📂 Project Structure
Week_3/
│
├── data/
│   └── Sample - Superstore.csv
│
├── week3_subqueries_cte_window_functions.ipynb
│
├── sql_queries.sql
│
├── superstore.db
│
└── README.md
📊 Dataset Information

Dataset Name: Sample Superstore Dataset

The dataset contains sales transaction details including:

Customer Information
Product Information
Orders
Sales
Quantity
Discount
Profit
Region
Category
Shipping Details
✅ Tasks Performed
Database Preparation
Imported Superstore CSV dataset
Created SQLite database
Loaded dataset into superstore_raw
Created normalized tables:
customers
orders
products
SQL Concepts Implemented
✔ Subqueries
Orders with above-average sales
Highest sales order for each customer
✔ Common Table Expressions (CTEs)
Total sales per customer
Customers above average sales
✔ Window Functions
ROW_NUMBER()
RANK()
✔ Business Queries
Top 10 Customers
Bottom 10 Customers
Customers with a Single Order
Customer Sales Ranking
Customer Ranking using JOIN + CTE + Window Functions
📈 Key Business Insights
Identified customers generating the highest revenue.
Ranked customers using SQL Window Functions.
Found customers whose sales exceed the overall average.
Determined customers with only one purchase.
Demonstrated how CTEs simplify complex SQL queries.
Applied Window Functions for advanced analytical reporting.
📄 Files Included
File	Description
week3_subqueries_cte_window_functions.ipynb	Complete implementation with outputs and business insights
sql_queries.sql	All SQL queries used in the assignment
superstore.db	SQLite database
Sample - Superstore.csv	Original dataset
README.md	Project documentation
▶️ How to Run
Clone the repository.
Open the project in VS Code.
Install required libraries.
pip install pandas jupyter
Open the notebook:
week3_subqueries_cte_window_functions.ipynb
Run all cells sequentially.
📌 Assignment Coverage
Requirement	Status
Load Dataset	✅
Create SQL Database	✅
Create Customers Table	✅
Create Orders Table	✅
Create Products Table	✅
SELECT DISTINCT	✅
Subqueries	✅
Common Table Expressions (CTEs)	✅
ROW_NUMBER()	✅
RANK()	✅
JOIN Operations	✅
Top Customers	✅
Low Customers	✅
Single Order Customers	✅
Above Average Sales	✅
Query Results	✅
Business Insights	✅

# Week 5 – PySpark Data Cleaning, Transformation & Aggregation

## Celebal Technologies Internship – Data Engineering

### Overview

This repository contains the Week 5 assignment completed as part of the Celebal Technologies Data Engineering Internship. The assignment demonstrates the use of Apache Spark (PySpark) for data cleaning, transformation, filtering, aggregation, schema modification, and building a simple data processing pipeline using DataFrames.

---

## Objectives

- Understand Apache Spark fundamentals
- Compare MapReduce and Spark
- Learn Spark DataFrames and their immutability
- Perform data cleaning operations
- Handle duplicate and missing values
- Apply filtering conditions
- Perform aggregation using DataFrame APIs
- Modify DataFrame schema
- Build a simple data processing pipeline

---

## Technologies Used

- Python
- Apache Spark (PySpark)
- Pandas
- Jupyter Notebook
- VS Code

---

## Dataset

- Sample - Superstore.csv

---

## Project Structure

```
Week_5
│
├── data/
│   └── Sample - Superstore.csv
│
├── pyspark_data_processing.ipynb
├── Assignment_Report.md
└── README.md
```

---

## Concepts Covered

- Spark Session
- DataFrames
- Schema Inspection
- Data Cleaning
- Duplicate Removal
- Null Value Handling
- Filtering
- Aggregation
- GroupBy
- Wide Transformations
- Shuffle Operations
- Schema Modification
- Data Processing Pipeline

---

## Files

| File | Description |
|------|-------------|
| pyspark_data_processing.ipynb | Complete implementation of all assignment questions |
| Assignment_Report.md | Detailed explanation of all tasks performed |
| Sample - Superstore.csv | Dataset used for the assignment |

---

# Week 6 Assignment Report
## Apache Spark Architecture and Data Processing

**Intern:** Gaurav Gaikwad  
**Internship:** Celebal Technologies – Data Engineering Internship  
**Week:** 6  
**Technology:** Apache Spark (PySpark)

---

# Objective

The objective of this assignment is to understand the architecture of Apache Spark and perform data processing using PySpark DataFrames. The assignment focuses on distributed computing concepts, Spark architecture, DataFrame transformations, actions, lazy evaluation, execution plans, and efficient data storage techniques.

---

# Problem Statement

Modern organizations generate massive amounts of structured and unstructured data that cannot be processed efficiently using traditional single-machine systems. Apache Spark provides a distributed computing framework capable of processing large datasets efficiently through in-memory computation and parallel execution.

The goal of this assignment is to explore Spark Architecture, understand its execution model, and implement various DataFrame operations while studying optimization techniques such as Lazy Evaluation, DAG execution, and Predicate Pushdown.

---

# Dataset

**Dataset Used:** Sample Superstore Dataset

The dataset contains sales transactions with information including:

- Order Details
- Customer Information
- Product Information
- Region
- Sales
- Profit
- Discount
- Quantity

---

# Tasks Performed

The following operations were successfully performed:

- Created a Spark Session
- Loaded CSV data into a Spark DataFrame
- Displayed sample records
- Printed DataFrame schema
- Renamed selected columns
- Changed data types using casting
- Added a new calculated column
- Filtered records using conditions
- Selected required columns
- Checked for null values
- Demonstrated Spark Transformations and Actions
- Explained Spark Execution Plan
- Demonstrated Lazy Evaluation
- Compared CSV and Parquet storage concepts
- Answered theoretical questions on Spark Architecture and optimization techniques

---

# Key Concepts Learned

During this assignment, the following Apache Spark concepts were explored:

- Spark Architecture
- Driver Program
- Cluster Manager
- Executors
- SparkSession
- DataFrame API
- Transformations
- Actions
- Lazy Evaluation
- Directed Acyclic Graph (DAG)
- Catalyst Optimizer
- Predicate Pushdown
- CSV vs Parquet
- Fault Tolerance
- Distributed Data Processing

---

# Challenges Faced

While implementing the assignment, the following challenges were encountered:

- Parsing issues while reading the CSV dataset due to formatting inconsistencies.
- Windows environment required Hadoop configuration (`HADOOP_HOME` and `winutils.exe`) for writing CSV and Parquet files.
- Some theory questions used generic DataFrames and column names (for example `df_orders`, `status`, `amount`, `base_price`, and `priority`) that were not part of the provided Superstore dataset. These were answered as Spark syntax examples while practical implementation was demonstrated using the available dataset.

---

# Outcome

The assignment provided practical exposure to Apache Spark and distributed data processing. It demonstrated how Spark efficiently processes large datasets using in-memory computation, lazy evaluation, optimized execution plans, and fault tolerance mechanisms.

The practical implementation strengthened understanding of DataFrame operations, Spark architecture, distributed execution, and performance optimization techniques commonly used in modern Big Data applications.

---

# Conclusion

This assignment successfully demonstrated the implementation of Apache Spark using PySpark for scalable data processing. Practical tasks such as loading data, transforming datasets, filtering records, and analyzing execution plans were completed successfully. In addition, theoretical concepts including Spark Architecture, Driver and Executor roles, DAG, Lazy Evaluation, Predicate Pushdown, and DataFrame operations were studied in detail. Overall, this assignment enhanced both conceptual understanding and practical skills required for building efficient Big Data processing pipelines using Apache Spark.

---

# Tools and Technologies

- Apache Spark
- PySpark
- Python
- Jupyter Notebook
- Pandas
- CSV Dataset
- Apache Parquet (Concept)

------------------------------------------------


# Week 7 Assignment Report
## Data Exploration and Cleaning using Pandas

**Intern:** Gaurav Gaikwad

---

# Objective

The objective of this assignment is to perform data exploration and data cleaning using the Pandas library. The assignment focuses on loading a dataset, exploring its structure, handling missing values, filtering data, removing duplicates, creating derived features, and exporting a cleaned dataset for further analysis.

---

# Dataset

**Dataset Used:** Sample Superstore Dataset

The dataset contains order details, customer information, product information, sales, quantity, profit, discount, shipping information, and regional details.

---

# Tasks Performed

- Loaded the CSV dataset using Pandas
- Explored the dataset using `head()`, `tail()`, `shape`, `columns`, and `info()`
- Examined data types
- Checked and handled missing values
- Filtered rows based on category
- Selected relevant columns
- Removed duplicate records
- Created a new column `total_amount = Sales × Quantity`
- Saved the cleaned dataset as a new CSV file

---

# Libraries Used

- Python
- Pandas
- Jupyter Notebook

---

# Outcome

The assignment provided practical experience with data exploration and preprocessing using Pandas. The cleaned dataset is now suitable for further analytics, visualization, or machine learning tasks.

---

# Conclusion

This assignment strengthened my understanding of Pandas DataFrames, data cleaning techniques, feature engineering, and CSV file operations. These preprocessing skills are fundamental for building reliable data analysis and machine learning workflows.

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

👨‍💻 Author

Gaurav Gaikwad

B.Tech Information Technology

Sanjivani College of Engineering

Celebal Technologies Internship 2026

