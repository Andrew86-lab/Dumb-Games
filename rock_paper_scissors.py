# Created by Andrewlab-86, date 2/27/25

import random

user_points = 0
ai_points = 0

while True:
    try:
        user_rounds = int(input("Enter the number of rounds you want to play: "))
        if user_rounds <= 0:
            print("Please enter a positive number of rounds.")
        else:
            break
    except ValueError:
        print("Please enter a valid number of rounds.")

choice = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

rounds_played = 0

while rounds_played < user_rounds:
    try:
        user_input = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
        if user_input not in [1, 2, 3]:
            print("Please enter a valid choice (1, 2, or 3).")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    ai_choice = random.randint(1, 3)

    print(f"You chose {choice[user_input]} and AI chose {choice[ai_choice]}.")

    if choice[user_input] == choice[ai_choice]:
        print("It's a tie!")
        user_points -= 1
        ai_points -= 1
    elif (choice[user_input] == "rock" and choice[ai_choice] == "scissors") or \
         (choice[user_input] == "paper" and choice[ai_choice] == "rock") or \
         (choice[user_input] == "scissors" and choice[ai_choice] == "paper"):
        print("You win this round!")
        user_points += 1
    else:
        print("You lose this round!")
        ai_points += 1

    rounds_played += 1
    print(f"Round {rounds_played}/{user_rounds} completed.")
    print(f"Current score -> You: {user_points}, AI: {ai_points}\n")

if user_points > ai_points:
    print(f"You win the game! Final score -> You: {user_points}, AI: {ai_points}")
elif user_points < ai_points:
    print(f"AI wins the game! Final score -> You: {user_points}, AI: {ai_points}")
else:
    print(f"The game is a tie! Final score -> You: {user_points}, AI: {ai_points}")