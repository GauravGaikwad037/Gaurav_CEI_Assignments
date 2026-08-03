-- Q1 Revenue by Category
SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category;


-- Q2 Top 10 Customers
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC
LIMIT 10;


-- Q3 Monthly Orders
SELECT
    substr(order_date,1,7) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY month;

-- Q4 Customers with Orders Not Delivered

SELECT
    customer_id,
    COUNT(*) AS pending_orders
FROM orders
WHERE status <> 'DELIVERED'
GROUP BY customer_id;

-- Q5 Return Rate by Region

SELECT
    region_code,
    COUNT(CASE WHEN status='RETURNED' THEN 1 END) AS returned_orders,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(CASE WHEN status='RETURNED' THEN 1 END) * 100.0 /
        COUNT(*),
        2
    ) AS return_rate
FROM orders
GROUP BY region_code;

-- Q6 Top Selling Products

SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM order_items
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 5;

-- Q7 Running Revenue

SELECT
    order_id,
    quantity * unit_price AS revenue,
    SUM(quantity * unit_price)
    OVER(
        ORDER BY order_id
    ) AS running_total
FROM order_items;

-- Q8 Dense Rank

SELECT
    product_id,
    SUM(quantity) AS total_sales,

    DENSE_RANK() OVER(

        ORDER BY SUM(quantity) DESC

    ) AS sales_rank

FROM order_items

GROUP BY product_id;

-- Q9 Lag

SELECT

    order_date,

    COUNT(*) AS orders,

    LAG(COUNT(*),1)

    OVER(

        ORDER BY order_date

    ) AS previous_day

FROM orders

GROUP BY order_date;

-- Q10 CTE

WITH revenue_cte AS(

SELECT

product_id,

SUM(quantity*unit_price) revenue

FROM order_items

GROUP BY product_id

)

SELECT *

FROM revenue_cte

ORDER BY revenue DESC;

-- Q11 NTILE

SELECT

product_id,

SUM(quantity) total_sales,

NTILE(4)

OVER(

ORDER BY SUM(quantity) DESC

) quartile

FROM order_items

GROUP BY product_id;

-- Q12 Average Order Value

SELECT

AVG(quantity*unit_price)

AS average_order_value

FROM order_items;

-- Q13 Highest Revenue Product

SELECT

product_id,

SUM(quantity*unit_price)

AS revenue

FROM order_items

GROUP BY product_id

ORDER BY revenue DESC

LIMIT 1;

-- Q14 Contribution Percentage

SELECT

product_id,

ROUND(

SUM(quantity*unit_price)*100.0/

(

SELECT

SUM(quantity*unit_price)

FROM order_items

),

2

) contribution

FROM order_items

GROUP BY product_id;

-- Q15 Customer Type

SELECT

customer_type,

COUNT(*)

total_customers

FROM customers

GROUP BY customer_type;

-- Q16 Self Join

SELECT

a.customer_id,

a.order_id,

b.order_id

FROM orders a

JOIN orders b

ON a.customer_id=b.customer_id

AND a.order_id<>b.order_id

LIMIT 20;