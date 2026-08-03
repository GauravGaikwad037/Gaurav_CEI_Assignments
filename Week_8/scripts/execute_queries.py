import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB = BASE_DIR / "database" / "ecommerce.db"

REPORT = BASE_DIR / "reports"

REPORT.mkdir(exist_ok=True)

conn = sqlite3.connect(DB)

query1 = """
SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category
"""

df1 = pd.read_sql_query(query1, conn)

print(df1)

query2 = """
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC
LIMIT 10
"""

df2 = pd.read_sql_query(query2, conn)

print(df2)

query3 = """
SELECT
    substr(order_date,1,7) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY month
"""

df3 = pd.read_sql_query(query3, conn)

print(df3)

with open(REPORT / "sql_results.md", "w") as file:

    file.write("# SQL Query Results\n\n")

    file.write("## Revenue by Category\n")

    file.write(df1.to_markdown(index=False))

    file.write("\n\n")

    file.write("## Top Customers\n")

    file.write(df2.to_markdown(index=False))

    file.write("\n\n")

    file.write("## Monthly Orders\n")

    file.write(df3.to_markdown(index=False))

print("SQL Results Saved")

conn.close()