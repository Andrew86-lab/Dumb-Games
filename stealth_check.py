import random

dice_ranges = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

try:
    user_dice = input("What dice are you using? D4, D6, D8, D10, D12, D20, D100: ").lower()

    if user_dice in dice_ranges:
        dice = random.randint(1, dice_ranges[user_dice])
        print(f"You rolled a {dice}.")
    else:
        print("Invalid dice type.")

except ValueError:
    print("Please enter a valid dice type.")