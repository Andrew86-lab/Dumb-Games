import random

proficiency_bonus = {
    1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4,
    11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6
}

def get_proficiency_bonus(level):
    return proficiency_bonus.get(level, 2)

def get_dexterity_modifier(dexterity, known_modifier):
    if known_modifier:
        return dexterity
    return (dexterity - 10) // 2

def main():
    dice = random.randint(1, 20)

    try:
        user_level = int(input("What is your character's level? "))
        if user_level not in proficiency_bonus:
            raise ValueError("Invalid level.")
    except ValueError as ve:
        print(ve)
        return

    user_input = input("Do you know your character's dexterity modifier? (Y/N) ").lower()

    if user_input in {"y", "n"}:
        try:
            user_dexterity = int(input(f"What is your character's dexterity {'modifier' if user_input == 'y' else 'score'}? "))
            if user_input == "n":
                user_dexterity = get_dexterity_modifier(user_dexterity, False)
        except ValueError:
            print("Invalid input.")
            return
    else:
        print("Invalid input.")
        return

    print(f"You rolled a d20 and got {dice}.")

    stealth_check = dice + user_dexterity + get_proficiency_bonus(user_level)
    print(f"Your stealth check is {stealth_check}.")

if __name__ == "__main__":
    main()