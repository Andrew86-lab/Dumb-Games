# Created by Andrew86-lab

import math
import random

dice = random.randint(1, 20)
user_level = input("What is your character's level? ")

try:
    user_level = int(user_level)
except ValueError:
    print("Invalid input. Please enter a number for the level.")
    exit()

proficiency_bonus = math.ceil((user_level / 4) + 1)

user_input = input("Do you know your character's dexterity modifier? (Y/N) ").lower().strip()

stealth_proficiency = input("Do you have proficiency in the Stealth skill? (Y/N) ").lower().strip()
stealth_expertise = "n"
if stealth_proficiency == "y":
    stealth_expertise = input("Do you have expertise in the Stealth skill? (Y/N) ").lower().strip()

user_dexterity = 0
if user_input == "y":
    try:
        user_dexterity = int(input("What is your character's dexterity modifier? ")).strip()
    except ValueError:
        print("Invalid input. Please enter a number for the dexterity modifier.")
        exit()
elif user_input == "n":
    try:
        dex_score = int(input("What is your character's dexterity score? ")).strip()
        user_dexterity = (dex_score - 10) // 2
    except ValueError:
        print("Invalid input. Please enter a number for the dexterity score.")
        exit()
else:
    print("Invalid input for dexterity modifier.")
    exit()

print(f"You rolled a {dice}")

stealth_check = dice + user_dexterity
if stealth_expertise == "y":
    stealth_check += (proficiency_bonus[user_level] * 2)
elif stealth_proficiency == "y":
    stealth_check += proficiency_bonus[user_level]

print(f"Your stealth check is {stealth_check}.")