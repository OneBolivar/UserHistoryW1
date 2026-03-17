
from Option1 import OptionNumber1
def OptionNumber2():
    print("\n--- PURCHASE SUMMARY ---")
    Inventory = []
    ProductData = OptionNumber1()
    Inventory.append(ProductData)
    TotalToPay = 0
    for Position in Inventory:
        print(f"Product: {Position[0]} | Unit Price: {Position[1]} | Quantity: {Position[2]} | Total to pay: {Position[3]}")
        TotalToPay = TotalToPay + Position[3]
        print("-" * 30)
        print("FINAL TOTAL TO PAY: $", TotalToPay)
