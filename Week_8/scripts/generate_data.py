import random
from faker import Faker
import pandas as pd
from pathlib import Path

fake = Faker()

random.seed(42)
Faker.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"

RAW_DATA.mkdir(parents=True, exist_ok=True)

NUM_CUSTOMERS = 500
NUM_PRODUCTS = 500
NUM_ORDERS = 500
NUM_ORDER_ITEMS = 1000

STATUS = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

CUSTOMER_TYPES = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]

CATEGORIES = [
    "Electronics",
    "Books",
    "Clothing",
    "Home"
]

REGIONS = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST"
]

def generate_customers():

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customers.append({

            "customer_id": f"C{i:04}",

            "customer_name": fake.name(),

            "email": fake.email(),

            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),

            "customer_type": random.choice(
                CUSTOMER_TYPES
            )

        })

    return pd.DataFrame(customers)

def generate_products():

    products = []

    categories = {
        "Electronics": ["Laptop", "Mouse", "Keyboard", "Monitor"],
        "Books": ["Python Book", "SQL Guide", "AI Handbook"],
        "Clothing": ["Shirt", "Jeans", "Jacket"],
        "Home": ["Chair", "Table", "Lamp"]
    }

    for i in range(1, NUM_PRODUCTS + 1):

        category = random.choice(list(categories.keys()))

        product = random.choice(categories[category])

        # Intentionally create inconsistent names
        if random.random() < 0.20:
            product = random.choice([
                product.lower(),
                product.upper(),
                " " + product,
                product + " "
            ])

        products.append({

            "product_id": f"P{i:04}",

            "product_name": product,

            "category": category,

            "subcategory": fake.word().title(),

            "cost_price": round(random.uniform(50, 5000), 2)

        })

    return pd.DataFrame(products)

def generate_orders():

    orders = []

    for i in range(1, NUM_ORDERS + 1):

        customer = f"C{random.randint(1, NUM_CUSTOMERS):04}"

        order_date = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        orders.append({

            "order_id": f"O{i:05}",

            "customer_id": customer,

            "order_date": order_date,

            "status": random.choice(STATUS),

            "region_code": random.choice(REGIONS)

        })

    return pd.DataFrame(orders)

def generate_order_items():

    items = []

    for i in range(1, NUM_ORDER_ITEMS + 1):

        items.append({

            "item_id": i,

            "order_id": f"O{random.randint(1, NUM_ORDERS):05}",

            "product_id": f"P{random.randint(1, NUM_PRODUCTS):04}",

            "quantity": random.randint(1, 10),

            "unit_price": round(random.uniform(100, 5000), 2),

            "discount_percent": random.randint(0, 50)

        })

    return pd.DataFrame(items)

def inject_bad_data(customers, orders, products, items):

    # Invalid Emails
    customers.loc[0, "email"] = "abcgmail.com"
    customers.loc[1, "email"] = "xyz@"

    # Missing Customer IDs
    orders.loc[0:24, "customer_id"] = None

    # Wrong Date Format
    orders.loc[5, "order_date"] = "32/13/2025"

    # Negative Quantity
    items.loc[0:29, "quantity"] = -5

    # Duplicate Orders
    orders = pd.concat([orders, orders.iloc[:5]])

    return customers, orders, products, items

def main():

    customers = generate_customers()

    products = generate_products()

    orders = generate_orders()

    items = generate_order_items()

    customers, orders, products, items = inject_bad_data(
        customers,
        orders,
        products,
        items
    )

    customers.to_csv(
        RAW_DATA / "customers.csv",
        index=False
    )

    products.to_csv(
        RAW_DATA / "products.csv",
        index=False
    )

    orders.to_csv(
        RAW_DATA / "orders.csv",
        index=False
    )

    items.to_csv(
        RAW_DATA / "order_items.csv",
        index=False
    )

    print("===================================")
    print("Data Generated Successfully")
    print("===================================")
    print(RAW_DATA)


if __name__ == "__main__":
    main()