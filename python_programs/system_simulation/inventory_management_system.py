number_of_products = int(input("Enter the number of products: "))
inventory = {}


for i in range(number_of_products):
    product_name = input(f"Enter the name of product {i + 1}: ").strip()
    quantity = int(input(f"Enter the quantity of product {i + 1}: "))

    if quantity < 0:
        print("Quantity cannot be negative. Setting to 0.")
        quantity = 0

    inventory[product_name] = quantity


update_product = input("\nEnter the product name to update: ").strip()
if update_product in inventory:
    new_quantity = int(input(f"Enter the new quantity for {update_product}: "))
    inventory[update_product] = new_quantity
else:
    print("Product not found in inventory.")


out_of_stock_products = [p for p, q in inventory.items() if q == 0]
total_inventory_items = sum(inventory.values())


print("\nUpdated Inventory:", inventory)
print("Out of Stock Products:", out_of_stock_products if out_of_stock_products else "None")
print("Total Inventory Items:", total_inventory_items)
