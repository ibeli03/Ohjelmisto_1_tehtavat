largest = None
smallest= None

user_input = input("Enter a number: ")
while user_input != "":
    number=float(user_input)
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

    user_input=input("Enter a number: ")
if largest is not None and smallest is not None:
    print(f"The largest number is {largest}")
    print(f"The smallest number is {smallest}")
else : print("No numbers entered")






