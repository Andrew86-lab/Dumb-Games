import random

rolls = int(input("How many times do you want to roll? "))
dice = int(input("Enter the number that you want the dice to be out of: "))

if dice > 0:
    while rolls > 0:
        number = random.randint(1, dice)
        print(f"Your roll was {number}")
        rolls -= 1
else:
    print("Please enter a valid number greater than 0 for the dice sides.")