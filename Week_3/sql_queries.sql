# /*

```
                CELEBAL TECHNOLOGIES INTERNSHIP 2026

                Week 3 Assignment
SQL-Based Data Analysis Using Subqueries, CTEs & Window Functions
```

======================================================================

Submission Files

1. week3_subqueries_cte_window_functions.ipynb

   * Complete implementation
   * Database creation
   * Table creation
   * Query execution
   * Query results
   * Business insights

2. sql_queries.sql

   * Contains all executable SQL queries only.

3. superstore.db

   * SQLite database used for analysis.

4. README.md

   * Assignment documentation.

---

NOTE

This SQL file contains only executable SQL statements.

For query outputs, execution results, and business insights,
please refer to:

week3_subqueries_cte_window_functions.ipynb

======================================================================
*/

---

## -- Q1 : Orders With Sales Greater Than Average Sales

SELECT *
FROM superstore_raw
WHERE Sales >
(
SELECT AVG(Sales)
FROM superstore_raw
);

---

## -- Q2 : Highest Order Of Each Customer

SELECT *
FROM superstore_raw s
WHERE Sales =
(
SELECT MAX(Sales)
FROM superstore_raw
WHERE "Customer ID" = s."Customer ID"
);

---

## -- Q3 : Total Sales Per Customer Using CTE

WITH CustomerSales AS
(
SELECT
"Customer ID",
"Customer Name",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
)

SELECT *
FROM CustomerSales
ORDER BY Total_Sales DESC;

---

## -- Q4 : Customers Above Average Total Sales

WITH CustomerSales AS
(
SELECT
"Customer ID",
"Customer Name",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
)

SELECT *
FROM CustomerSales
WHERE Total_Sales >
(
SELECT AVG(Total_Sales)
FROM CustomerSales
);

---

## -- Q5 : ROW_NUMBER() Based On Sales

SELECT
"Customer Name",
Sales,
ROW_NUMBER()
OVER
(
ORDER BY Sales DESC
) AS Row_Number
FROM superstore_raw;

---

## -- Q6 : Ranking Customers Based On Sales

SELECT
"Customer Name",
Sales,
RANK()
OVER
(
ORDER BY Sales DESC
) AS Sales_Rank
FROM superstore_raw;

---

## -- Q7 : Top 10 Customers Based On Total Sales

WITH CustomerSales AS
(
SELECT
"Customer ID",
"Customer Name",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
)

SELECT *
FROM CustomerSales
ORDER BY Total_Sales DESC
LIMIT 10;

---

## -- Q8 : Bottom 10 Customers Based On Total Sales

WITH CustomerSales AS
(
SELECT
"Customer ID",
"Customer Name",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
)

SELECT *
FROM CustomerSales
ORDER BY Total_Sales ASC
LIMIT 10;

---

## -- Q9 : Customers Who Placed Only One Order

SELECT
"Customer ID",
"Customer Name",
COUNT("Order ID") AS Orders
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
HAVING Orders = 1;

---

## -- Q10 : Customer Ranking Based On Total Sales

WITH CustomerSales AS
(
SELECT
"Customer ID",
"Customer Name",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID",
"Customer Name"
)

SELECT
*,
RANK()
OVER
(
ORDER BY Total_Sales DESC
) AS Customer_Rank
FROM CustomerSales;

---

## -- Q11 : Customer Sales Ranking Using JOIN + CTE + Window Function

WITH CustomerSales AS
(
SELECT
"Customer ID",
SUM(Sales) AS Total_Sales
FROM superstore_raw
GROUP BY
"Customer ID"
)

SELECT
c."Customer ID",
c."Customer Name",
cs.Total_Sales,
RANK()
OVER
(
ORDER BY cs.Total_Sales DESC
) AS Customer_Rank
FROM customers c
JOIN CustomerSales cs
ON c."Customer ID" = cs."Customer ID"
ORDER BY Customer_Rank;
