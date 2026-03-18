from Option1 import OptionNumber1
from Option2 import inventory_print
import Option2
from Option3 import calculate_statistics

def MenuOptions():
    VALIDATOR = True
    while VALIDATOR:
        print("                   Welcome")
        print("=" * 50)
        print("=" * 50)
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculates statistics")
        print("4. Exit")
        
        #---------------------------------------------------------
        VALIDATOR_OPTIONS = True
        try:
            while VALIDATOR_OPTIONS:
                Options = float(input("What do you want to do?: "))
                print("      ")
                if (Options <= 0) or (Options > 4):
                    int("Force Error") 
                elif Options == 1:
                    Option2.Inventory.update(OptionNumber1(Options))
                    
                elif Options == 2:
                    inventory_print()
                elif Options == 3:
                    calculate_statistics()
                elif Options == 4:
                    print("AQUI VA LA OPCION 4")                
         
        #------------------------------------------------------------        
        except ValueError:
            print("---------------------------------------")
            print("Error only shows the displayed options")
            print("---------------------------------------")
            print("     ")

