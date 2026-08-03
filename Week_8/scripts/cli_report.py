import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "ecommerce.db"

conn = sqlite3.connect(DB_PATH)

def menu():

    print("\n======================================")
    print(" E-Commerce Order Analytics System ")
    print("======================================")

    print("1. Daily Report")
    print("2. Weekly Report")
    print("3. Monthly Report")
    print("4. Exit")
    
def daily_report():

    print("\nDaily Report\n")

    total_orders = pd.read_sql_query(
        "SELECT COUNT(*) AS Total_Orders FROM orders",
        conn
    )

    revenue = pd.read_sql_query(
        """
        SELECT
        SUM(quantity * unit_price) AS Revenue
        FROM order_items
        """,
        conn
    )

    customers = pd.read_sql_query(
        """
        SELECT
        COUNT(DISTINCT customer_id)
        AS Customers
        FROM orders
        """,
        conn
    )

    products = pd.read_sql_query(
        """
        SELECT
        product_id,
        SUM(quantity) AS Total_Sold
        FROM order_items
        GROUP BY product_id
        ORDER BY Total_Sold DESC
        LIMIT 3
        """,
        conn
    )

    print(total_orders)

    print(revenue)

    print(customers)

    print("\nTop 3 Products")

    print(products)
    
def weekly_report():

    print("\nWeekly Report\n")

    daily_report()
    
def monthly_report():

    print("\nMonthly Report\n")

    daily_report()
    
while True:

    menu()

    choice = input("\nEnter your choice : ")

    if choice == "1":

        daily_report()

    elif choice == "2":

        weekly_report()

    elif choice == "3":

        monthly_report()

    elif choice == "4":

        print("\nThank You!")

        break

    else:

        print("\nInvalid Choice")
        
conn.close()