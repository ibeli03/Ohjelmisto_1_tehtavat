numbers = []

while True:
    user_input = input("Enter a number or press enter to continue: ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please enter a valid number.")
numbers.sort(reverse=True)
top_5_numbers=numbers[:5]

print(f"The top 5 numbers in descending order are {top_5_numbers}")


