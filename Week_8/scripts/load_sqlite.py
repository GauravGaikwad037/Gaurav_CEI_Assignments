import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN = BASE_DIR / "data" / "cleaned"

DATABASE = BASE_DIR / "database"

DATABASE.mkdir(exist_ok=True)

DB_PATH = DATABASE / "ecommerce.db"

conn = sqlite3.connect(DB_PATH)

print("Database Connected Successfully")

customers = pd.read_csv(CLEAN / "customers_clean.csv")

products = pd.read_csv(CLEAN / "products_clean.csv")

orders = pd.read_csv(CLEAN / "orders_clean.csv")

order_items = pd.read_csv(CLEAN / "order_items_clean.csv")

customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

order_items.to_sql(
    "order_items",
    conn,
    if_exists="replace",
    index=False
)

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()

print("\nTables Created Successfully:\n")

for table in tables:
    print(table[0])
    
for table in [
    "customers",
    "products",
    "orders",
    "order_items"
]:

    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )

    print(f"\n{table}")

    print(count)
    
for table in [
    "customers",
    "products",
    "orders",
    "order_items"
]:

    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )

    print(f"\n{table}")

    print(count)
    
conn.close()

print("\nDatabase Saved Successfully")

print(DB_PATH)