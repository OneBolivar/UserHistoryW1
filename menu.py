from Option1 import OptionNumber1 # Importa la función OptionNumber1 del módulo Option1
from Option2 import inventory_print # Importa la función para imprimir el inventario de Option2
import Option2 # Importa el módulo Option2 completo para acceder a sus variables
from Option3 import calculate_statistics # Importa la función de estadísticas del módulo Option3

def MenuOptions(): # Define la función principal que maneja el menú
    VALIDATOR = True # Variable de control para mantener el bucle principal activo
    while VALIDATOR: # Inicia el bucle que repetirá el menú hasta que se decida salir
        print("                   Welcome") # Muestra el mensaje de bienvenida
        print("=" * 50) # Imprime una línea decorativa de 50 símbolos de igual
        print("=" * 50) # Imprime una segunda línea decorativa
        print("1. Add product") # Opción 1: Agregar producto
        print("2. Show inventory") # Opción 2: Mostrar inventario
        print("3. Calculates statistics") # Opción 3: Calcular estadísticas
        print("4. Exit") # Opción 4: Salir del programa
        
        #---------------------------------------------------------
        VALIDATOR_OPTIONS = True # Variable para validar la entrada del usuario
        try: # Inicia bloque para manejo de errores (por si el usuario ingresa letras)
            while VALIDATOR_OPTIONS: # Bucle para procesar la selección del usuario
                Options = float(input("What do you want to do?: ")) # Pide la opción y la convierte a decimal
                print("      ") # Espacio en blanco para mejorar la visualización
                if (Options <= 0) or (Options > 4): # Valida que el número esté entre 1 y 4
                    int("Force Error") # Si el número es inválido, fuerza un error para ir al except
                elif Options == 1: # Si elige 1
                    Option2.Inventory.update(OptionNumber1(Options)) # Actualiza el inventario con lo que retorne OptionNumber1
                    
                elif Options == 2: # Si elige 2
                    inventory_print() # Llama a la función que muestra los productos en pantalla
                elif Options == 3: # Si elige 3
                    calculate_statistics() # Ejecuta la función que procesa los datos numéricos
                elif Options == 4: # Si elige 4
                    print("AQUI VA LA OPCION 4") # Mensaje temporal para la función de salida
         
        #------------------------------------------------------------        
        except ValueError: # Se ejecuta si el usuario ingresa algo que no es un número o una opción inválida
            print("---------------------------------------") # Separador de error
            print("Error only shows the displayed options") # Mensaje de error al usuario
            print("---------------------------------------") # Separador de error
            print("     ") # Espacio en blanco
