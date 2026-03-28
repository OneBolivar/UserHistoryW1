
def product_update(Inventory, name):
    # PRODUCT UPDATE: Modify price and/or quantity of existing product
    # Allows partial updates (price only, quantity only, or both)
    VALIDATOR = True
    VALIDATOR_FALSE = False
    VALIDATOR_X =False
    
    # CRITICAL CHECK: Verify product exists before attempting update
    producto = Inventory.get(name)
    
    if not producto:
        print(f" Product '{name}' not found.")
        return VALIDATOR_FALSE
    

    print(f"\nUpdate: {name} (Price: {producto['price']}, Stock: {producto['quantity']})")
    print("1. Change Price")
    print("2. Change Stock")
    print("3. Change Both")
    
    option = input("Choose an option: ")

    # UPDATE LOGIC: Modify selected fields directly in the dictionary
    if option == "1":
        producto["price"] = float(input("New price: "))
    elif option == "2":
        producto["quantity"] = int(input("New stock: "))
    elif option == "3":
        producto["price"] = float(input("New price: "))
        producto["quantity"] = int(input("New stock: "))
    else:
        print("Invalid option.")
        return VALIDATOR_X

    print(" Update successful.")
    return VALIDATOR




