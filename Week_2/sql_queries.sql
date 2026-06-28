/*
------------------------------------------------------------

Submission Contents:
1. sql_queries.sql               -> Contains all SQL queries.
2. ecommerce_sales_database.ipynb -> Contains database creation,
   query execution, query results, and business insights.
3. ecommerce.db                  -> SQLite database used for analysis.

Note:

The corresponding query outputs and analysis are available in
'ecommerce_sales_database.ipynb'  Please check that file for Outputs.
This SQL file contains only executable SQL queries.


Author: Gaurav Gaikwad
------------------------------------------------------------
*/




-- Q1
SELECT * FROM customers;

-- Q2
SELECT first_name, last_name, city
FROM customers;

-- Q3
SELECT DISTINCT category
FROM products;

-- Q4 Primary Keys

customers → customer_id
products → product_id
orders → order_id
order_items → item_id

Primary Key uniquely identifies each record.

-- Q5 Foreign Keys

orders.customer_id → customers.customer_id
order_items.order_id → orders.order_id
order_items.product_id → products.product_id

Foreign Keys maintain relationships between tables.

-- Q6
SELECT *
FROM customers
WHERE is_premium = 1;

-- Q7
SELECT *
FROM products
WHERE unit_price > 1000;

-- Q8
SELECT *
FROM orders
WHERE order_date > '2024-08-15';

-- Q9
SELECT *
FROM customers
WHERE state = 'Maharashtra';

-- Q10
SELECT *
FROM orders
WHERE total_amount BETWEEN 2000 AND 6000;

-- Q11 Difference Between WHERE and HAVING

WHERE filters rows before aggregation.
HAVING filters groups after aggregation.

Example:
WHERE Sales > 1000
HAVING SUM(Sales) > 5000

-- Q12 Difference Between COUNT(*) and COUNT(column)

COUNT(*) counts all rows.
COUNT(column) counts only non-null values in that column.

-- Q13
SELECT
SUM(total_amount) AS Total_Sales
FROM orders;

-- Q14
SELECT
AVG(unit_price) AS Average_Price
FROM products;

-- Q15
SELECT
customer_id,
COUNT(order_id) AS Total_Orders
FROM orders
GROUP BY customer_id;

-- Q16
SELECT
category,
SUM(unit_price) AS Revenue
FROM products
GROUP BY category;

-- Q17
SELECT
category,
MAX(unit_price) AS Max_Price
FROM products
GROUP BY category;

-- Q18
SELECT
product_id,
SUM(quantity) AS Total_Quantity
FROM order_items
GROUP BY product_id;

-- Q19
SELECT *
FROM products
ORDER BY unit_price DESC
LIMIT 5;

-- Q20
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 3;

-- Q21
SELECT
c.customer_id,
c.first_name,
c.last_name,
SUM(o.total_amount) AS Total_Spending
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY Total_Spending DESC;

-- Q22 Difference Between INNER JOIN and LEFT JOIN

INNER JOIN returns only matching records from both tables.
LEFT JOIN returns all records from the left table and matching records from the right table.
If no match exists, NULL values are returned from the right table.

-- Q23
SELECT
strftime('%Y-%m', order_date) AS Month,
SUM(total_amount) AS Total_Sales
FROM orders
GROUP BY Month
ORDER BY Month;

-- Q24
SELECT
status,
COUNT(*) AS Total_Orders
FROM orders
GROUP BY status;

-- Q25
SELECT
c.first_name,
c.last_name,
o.order_id,
o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.is_premium = 1;

-- Q26
SELECT
email,
COUNT(*) AS Count_Email
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- Q27
SELECT COUNT(*) AS Total_Customers
FROM customers;

SELECT COUNT(*) AS Total_Products
FROM products;

SELECT COUNT(*) AS Total_Orders
FROM orders;

SELECT COUNT(*) AS Total_Order_Items
FROM order_items;