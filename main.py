#Declaramos una Variable llamada VALIDADOR como Verdadera
VALIDADOR = True
#Pedimos el nombre de el producto con el input
NombreProducto = input("Ingrese el nombre del producto: ")   
#Creamos un bucle While con VALIDADOR para que se repita el proceso que queremos 
while VALIDADOR:
#Iniciamos un try para solucionar un error que se explicara mas adelante     
    try:
#Creamos el paramatro "PrecioProducto"para pedir el precio del producto
        PrecioProducto = float(input("Ingrese el precio del producto: "))
#Creamos el paramatro "CantidadProducto"para pedir la cantidad del producto
        CantidadProducto = int(input("¿Cuantos productos desea comprar?: "))
#Creamos el parametro Total para hacer el proceso de Precio * Cantidad (producto)
        Total = PrecioProducto*CantidadProducto
#Imprimimos en pantalla el nombre del producto, precio unitario, la cantidad a comprar y el total a pagar        
        print("Producto:",NombreProducto,"|Precio Unitario:",PrecioProducto,"|Cantidad:",CantidadProducto,"|Total a pagar:",Total )
#Colocamos el validador y lo convertimos en falso para que se acabe el ciclo una vez cumplido el proceso              
        VALIDADOR = False
#Agregamos el except con el ValueError para que cuando ingresen un dato incorrecto el nos muestre el error
    except ValueError:
#Mostramos en consola el mensaje con el error y lo que debe hacer       
        print("¡ERROR! Debe ingresar un número")


   