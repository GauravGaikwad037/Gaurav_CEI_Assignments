import re
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN = BASE_DIR / "data" / "cleaned"

REPORTS = BASE_DIR / "reports"

REPORTS.mkdir(exist_ok=True)

customers = pd.read_csv(CLEAN / "customers_clean.csv")

orders = pd.read_csv(CLEAN / "orders_clean.csv")

products = pd.read_csv(CLEAN / "products_clean.csv")

order_items = pd.read_csv(CLEAN / "order_items_clean.csv")

def validate_emails(df):

    print("Checking Emails...")

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    invalid = df[
        ~df["email"].astype(str).str.match(pattern)
    ]

    return invalid

def check_referential_integrity(orders_df, items_df):

    print("Checking Foreign Keys...")

    invalid = items_df[
        ~items_df["order_id"].isin(
            orders_df["order_id"]
        )
    ]

    return invalid

def check_negative_quantity(df):

    return df[
        df["quantity"] < 0
    ]
    
def check_invalid_dates(df):

    invalid = df[
        df["order_date"].isna()
    ]

    return invalid

invalid_emails = validate_emails(customers)

broken_keys = check_referential_integrity(
    orders,
    order_items
)

negative_quantity = check_negative_quantity(
    order_items
)

invalid_dates = check_invalid_dates(
    orders
)

report = f"""
==============================
DATA VALIDATION REPORT
==============================

Invalid Emails      : {len(invalid_emails)}

Broken Foreign Keys : {len(broken_keys)}

Negative Quantity   : {len(negative_quantity)}

Invalid Dates       : {len(invalid_dates)}
"""

with open(
    REPORTS / "issues_report.txt",
    "w"
) as file:

    file.write(report)

print(report)

print("Report Saved Successfully")
    
    
    
      