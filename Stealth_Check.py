import random

dice = random.randint(1, 20)

user_level = int(input("What is your character's level? "))

proficiency_bonus = {
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 3,
    8: 3,
    9: 4,
    10: 4,
    11: 4,
    12: 4,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 6,
    18: 6,
    19: 6,
    20: 6
}

user_input = input("Do you know your character's dextererity modifier? (Y/N) ").lower()

if user_input == "y":
    user_dexterity = int(input("What is your chacacter's dexterity modifier? "))
elif user_input == "n":
    user_dexterity = int(input("What is your character's dexterity level? "))
    user_dexterity = (user_dexterity - 10) // 2
else:
    print("Invalid input.")

print(f"You rolled a {dice}")

stealth_check = dice + user_dexterity + (proficiency_bonus[user_level] * 2)

print(f"Your stealth check is {stealth_check}.")