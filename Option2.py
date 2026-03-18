Inventory = {} # Crea un diccionario global vacío para almacenar todos los productos
def inventory_print(): # Define la función que imprimirá el contenido del inventario
    product_added = {} # Crea un diccionario local temporal
    product_added.update(Inventory) # Copia el contenido del inventario global al diccionario local
    print("---------------------------------------------------------") # Imprime una línea decorativa
    print("Here are your inventory") # Muestra el encabezado del reporte de inventario
    for product, details in product_added.items(): # Inicia un bucle para recorrer cada producto y sus detalles
        print(f"Product: {product}") # Imprime el nombre del producto actual
        print(f"  Price: {details['price']} by unit") # Imprime el precio unitario del producto
        print(f"  Quantity: {details['quantity']}") # Imprime la cantidad disponible del producto
        #total = (details['price'] * details['quantity']) # Línea comentada: cálculo del total por producto
    #print(total) # Línea comentada: impresión del total calculado
    print("---------------------------------------------------------") # Imprime una línea decorativa de cierre
    print("---------------------------------------------------------") # Imprime una segunda línea decorativa
    print("Exiting the inventory management system.") # Muestra mensaje de salida del sistema de gestión
    print(" ") # Imprime un espacio en blanco para mejorar la legibilidad
    return # Finaliza la ejecución de la función y regresa al menú
