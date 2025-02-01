import random
def dice (sides):
        return random.randint(1, sides)
def main():
    sides = int(input("How many sides for a dice? "))
    result = 0
    while result != sides:
        result = dice(sides)
        print(f"Rolled: {result}")
if __name__ == "__main__":
    main()







