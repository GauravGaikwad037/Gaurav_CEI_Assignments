import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"

CLEAN = BASE_DIR / "data" / "cleaned"

CLEAN.mkdir(exist_ok=True)

orders = pd.read_csv(RAW / "orders.csv")

customers = pd.read_csv(RAW / "customers.csv")

products = pd.read_csv(RAW / "products.csv")

order_items = pd.read_csv(RAW / "order_items.csv")

def clean_orders(df):

    print("Cleaning Orders...")

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print("Duplicates Removed :", before - after)

    df["customer_id"] = df["customer_id"].fillna("UNKNOWN")

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    return df

def clean_products(df):

    print("Cleaning Products...")

    df["product_name"] = (

        df["product_name"]

        .astype(str)

        .str.strip()

        .str.title()

    )

    return df

def clean_order_items(df):

    print("Cleaning Order Items...")

    df["quantity"] = df["quantity"].clip(lower=0)

    return df

def clean_customers(df):

    print("Cleaning Customers...")

    df["customer_name"] = (

        df["customer_name"]

        .astype(str)

        .str.title()

    )

    return df

orders = clean_orders(orders)

products = clean_products(products)

order_items = clean_order_items(order_items)

customers = clean_customers(customers)

orders.to_csv(
    CLEAN / "orders_clean.csv",
    index=False
)

products.to_csv(
    CLEAN / "products_clean.csv",
    index=False
)

customers.to_csv(
    CLEAN / "customers_clean.csv",
    index=False
)

order_items.to_csv(
    CLEAN / "order_items_clean.csv",
    index=False
)

print()

print("============================")

print("Cleaning Completed")

print("============================")

print(CLEAN)