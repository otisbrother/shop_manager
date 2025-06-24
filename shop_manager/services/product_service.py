import json
import os
from models.product import Product

DATA_FILE = "data/products.json"

def load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_products(products):
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=2)

def add_product(product):
    products = load_products()
    products.append(product.to_dict())
    save_products(products)

def get_all_products():
    return load_products()

def update_product(product_id, name=None, price=None, quantity=None):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            if name: p["name"] = name
            if price: p["price"] = price
            if quantity: p["quantity"] = quantity
    save_products(products)

def delete_product(product_id):
    products = load_products()
    products = [p for p in products if p["id"] != product_id]
    save_products(products) 