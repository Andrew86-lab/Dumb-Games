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
        user_dexterity = int(input("What is your character's dexterity modifier? ").strip())
    except ValueError:
        print("Invalid input. Please enter a number for the dexterity modifier.")
        exit()
elif user_input == "n":
    try:
        dex_score = int(input("What is your character's dexterity score? ").strip())
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
    stealth_check += (proficiency_bonus * 2)
elif stealth_proficiency == "y":
    stealth_check += proficiency_bonus

print(f"Your stealth check is {stealth_check}.")

enemy_stat_block = input("Do you know the enemy's stat block? (Y/N)").lower().strip()
if enemy_stat_block not in ['y', 'n']:
    print("Invalid input for stat block. Please enter 'Y' or 'N'.")
    exit()

if enemy_stat_block == "n":
    try:
        enemy_challenge_rating = float(input("What is the challenge rating of the enemy? ").strip())

        if enemy_challenge_rating == 0:
            enemy_bonus = 2
        elif enemy_challenge_rating > 0:
            enemy_bonus = math.ceil(enemy_challenge_rating / 4) + 1
        else:
            print("Invalid input for challenge rating.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a number for the challenge rating.")
        exit()

    enemy_check = random.randint(1, 20)

    try:
        dm = input("Do you know the enemy's wisdom modifier? (Y/N) ").lower().strip()

        if dm == "y":
            try:
                enemy_wisdom = int(input("What is the enemy's wisdom modifier? ").strip())
            except ValueError:
                print("Invalid input. Please enter a number for the wisdom modifier.")
                exit()
        elif dm == "n":
            try:
                enemy_wisdom = int(input("What is your enemy's wisdom score? ").strip())
                enemy_wisdom = (enemy_wisdom - 10) // 2
            except ValueError:
                print("Invalid input. Please enter a number for the wisdom score.")
                exit()
        else:
            print("Invalid input for wisdom modifier.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a number for the wisdom modifier.")
        exit()

    enemy_perception = enemy_check + enemy_wisdom + enemy_bonus

    print(f"The enemy rolled a {enemy_check} and the enemy's perception check is {enemy_perception}.")
elif enemy_stat_block == "y":
    try:
        enemy_perception = int(input("What is the enemy's perception check? ").strip())
    except ValueError:
        print("Invalid input. Please enter a number for the perception check.")
        exit()

if stealth_check > enemy_perception:
    print("You are hidden from the enemy.")
else:
    print("You failed the stealth check.")