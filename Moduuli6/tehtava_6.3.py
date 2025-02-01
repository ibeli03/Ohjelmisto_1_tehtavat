

def gallons(american):
    return american*3.785

def main():
    while True:
        american = float(input("Enter the amount in gallons (input a negative value to end): "))
        if american < 0:
            break

        liters = gallons(american)
        print(f"{american} gallons are equivalent to {liters:.2f} liters.")
main()

