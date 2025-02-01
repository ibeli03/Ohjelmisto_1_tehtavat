import math

def calculate_unit_price(diameter, price):
    r = diameter / 2

    area = math.pi*(r*r)

    unit_price = price / area
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
price1 = float(input("Enter the price of the first pizza in euros: "))

diameter2=float(input("Enter the diameter of the second pizza in cm: "))
price2=float(input("Enter the price of the second pizza in euros: "))

unit_price=calculate_unit_price(diameter1, price1)
unit_price2=calculate_unit_price(diameter2, price2)
if unit_price>unit_price2:
    print("The second pizza has better value for money.")
else: print("The first pizza has better value for money.")

