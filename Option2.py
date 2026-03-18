Inventory = {}
def inventory_print():
    product_added = {}
    product_added.update(Inventory)
    print("---------------------------------------------------------")
    print("Here are your inventory")
    for product, details in product_added.items():
        print(f"Product: {product}")
        print(f"  Price: {details['price']} by unit")
        print(f"  Quantity: {details['quantity']}")
        #total = (details['price'] * details['quantity'])
    #print(total)
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Exiting the inventory management system.")
    print(" ")
    return