import random
number = random.randint(1, 10)
guess= None

while number != guess:
    guess=int(input("Guess the number between 1 and 10: "))

    if number > guess:
        print("Number is too low")
    elif number < guess:
        print("Number is too high")

else:
    print("Number is correct")







