import Option2

def calculate_statistics():
    total = 0
    product_added = {}
    product_added.update(Option2.Inventory)
    print("---------------------------------------------------------")
    print("Here are your statistics")
    for product, details in product_added.items():
        total += float((details['price'] * details['quantity']))
        
    print("")
    print("---------------------------------------------------------")
    print(total) 
    print("---------------------------------------------------------")
    print("")
    return

