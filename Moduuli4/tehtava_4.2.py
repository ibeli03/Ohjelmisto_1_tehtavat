inches = 0
while inches <= 0:
    inches = float(input("Enter inches: "))
    if inches < 0:
        print("Program exited")
    else:
        cm = inches*2.54
        print(f"{inches} equals {cm} centimeters")








