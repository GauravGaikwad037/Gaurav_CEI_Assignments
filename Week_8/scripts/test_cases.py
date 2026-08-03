import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN = BASE_DIR / "data" / "cleaned"

orders = pd.read_csv(CLEAN / "orders_clean.csv")

customers = pd.read_csv(CLEAN / "customers_clean.csv")

products = pd.read_csv(CLEAN / "products_clean.csv")

order_items = pd.read_csv(CLEAN / "order_items_clean.csv")

def test_invalid_order():

    print("\nTEST 1 : Invalid Order IDs")

    invalid = order_items[
        ~order_items["order_id"].isin(
            orders["order_id"]
        )
    ]

    print("Invalid Orders :", len(invalid))
    
def test_negative_quantity():

    print("\nTEST 2 : Negative Quantity")

    negative = order_items[
        order_items["quantity"] < 0
    ]

    print("Negative Quantity :", len(negative))
    
def test_invalid_email():

    print("\nTEST 3 : Invalid Emails")

    invalid = customers[
        ~customers["email"].str.contains("@")
    ]

    print("Invalid Emails :", len(invalid))
    
def test_missing_customer():

    print("\nTEST 4 : Missing Customer")

    missing = orders[
        orders["customer_id"] == "UNKNOWN"
    ]

    print("Unknown Customers :", len(missing))
    
def test_duplicate_products():

    print("\nTEST 5 : Duplicate Products")

    duplicates = products[
        products.duplicated(
            subset=["product_name"]
        )
    ]

    print("Duplicate Products :", len(duplicates))
    
    print("="*45)

print("RUNNING ALL TEST CASES")

print("="*45)

test_invalid_order()

test_negative_quantity()

test_invalid_email()

test_missing_customer()

test_duplicate_products()

print("\n")

print("="*45)

print("ALL TESTS COMPLETED")

print("="*45)