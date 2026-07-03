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
👨‍💻 Author

Gaurav Gaikwad

B.Tech Information Technology

Sanjivani College of Engineering

Celebal Technologies Internship 2026

⭐ This repository showcases my practical understanding of SQL for business analytics using Subqueries, Common Table Expressions (CTEs), and Window Functions on a real-world sales dataset.
