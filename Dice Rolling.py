import random

try:
    rolls = int(input("How many times do you want to roll? "))
    dice = int(input("Enter the number that you want the dice to be out of: "))

    if rolls <= 0:
        print("Please enter a valid number greater than 0 for the number of rolls.")
    elif dice <= 0:
        print("Please enter a valid number greater than 0 for the dice sides.")
    else:
        while rolls > 0:
            number = random.randint(1, dice)
            print(f"Your roll was {number}")
            rolls -= 1
except ValueError:
    print("Please use numbers")
