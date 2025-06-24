from services.product_service import *
from models.product import Product

def menu():
    print("\n=== SHOP MANAGER ===")
    print("1. Add product")
    print("2. View all products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose: ")
    
    if choice == "1":
        pid = input("Product ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(Product(pid, name, price, quantity))
        print("✅ Product added.")

    elif choice == "2":
        products = get_all_products()
        for p in products:
            print(p)

    elif choice == "3":
        pid = input("Enter ID to update: ")
        name = input("New name (Enter to skip): ")
        price = input("New price (Enter to skip): ")
        quantity = input("New quantity (Enter to skip): ")
        update_product(pid,
            name if name else None,
            float(price) if price else None,
            int(quantity) if quantity else None
        )
        print("✅ Product updated.")

    elif choice == "4":
        pid = input("Enter ID to delete: ")
        delete_product(pid)
        print("🗑️ Product deleted.")

    elif choice == "5":
        break

    else:
        print("❌ Invalid choice.") 