import random
number_dice = int(input("Enter the number of dice to roll: "))
total = 0
for _ in range(number_dice):
    roll = random.randint(1,6)
    total += roll
print(f"The total sum of the dice is: {total}")
