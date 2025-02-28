# Created by Andrewlab-86, date 2/27/25

import random

def get_valid_rounds():
    while True:
        try:
            rounds = int(input("Enter the number of rounds you want to play: "))
            if rounds <= 0:
                print("Please enter a positive number of rounds.")
            else:
                return rounds
        except ValueError:
            print("Please enter a valid number of rounds.")

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
            if user_choice in [1, 2, 3]:
                return user_choice
            else:
                print("Please enter a valid choice (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid number.")
            continue

def play_game():
    user_points = 0
    ai_points1 = 0
    ai_points2 = 0

    user_input1 = input("Do you want to play the game? (Y/N) ").lower()

    if user_input1 == "y":
        print("In this game, ties result in a penalty. Both players lose 1 point.")
        user_rounds = get_valid_rounds()
        choice = {1: "rock", 2: "paper", 3: "scissors"}
        rounds_played = 0

        while rounds_played < user_rounds:
            user_input2 = get_user_choice()
            ai_choice = random.randint(1, 3)

            print(f"You chose {choice[user_input2]} and AI chose {choice[ai_choice]}.")

            if choice[user_input2] == choice[ai_choice]:
                print("It's a tie! Both lose 1 point.")
                user_points -= 1
                ai_points1 -= 1
            elif (choice[user_input2] == "rock" and choice[ai_choice] == "scissors") or \
                 (choice[user_input2] == "paper" and choice[ai_choice] == "rock") or \
                 (choice[user_input2] == "scissors" and choice[ai_choice] == "paper"):
                print("You win this round!")
                user_points += 1
            else:
                print("You lose this round!")
                ai_points1 += 1

            rounds_played += 1
            print(f"Round {rounds_played}/{user_rounds} completed.")
            print(f"Current score -> You: {user_points}, AI: {ai_points1}\n")

        # Final result after all rounds
        if user_points > ai_points1:
            print(f"You win the game! Final score -> You: {user_points}, AI: {ai_points1}")
        elif user_points < ai_points1:
            print(f"AI wins the game! Final score -> You: {user_points}, AI: {ai_points1}")
        else:
            print(f"The game is a tie! Final score -> You: {user_points}, AI: {ai_points1}")
    
    elif user_input1 == "n":
        user_rounds = get_valid_rounds()
        choice = {1: "rock", 2: "paper", 3: "scissors"}
        rounds_played = 0

        while rounds_played < user_rounds:
            ai_choice1 = random.randint(1, 3)
            ai_choice2 = random.randint(1, 3)

            print(f"AI1 chose {choice[ai_choice1]} and AI2 chose {choice[ai_choice2]}.")

            if choice[ai_choice1] == choice[ai_choice2]:
                print("It's a tie! Both AIs lose 1 point.")
                ai_points1 -= 1
                ai_points2 -= 1
            elif (choice[ai_choice1] == "rock" and choice[ai_choice2] == "scissors") or \
                 (choice[ai_choice1] == "paper" and choice[ai_choice2] == "rock") or \
                 (choice[ai_choice1] == "scissors" and choice[ai_choice2] == "paper"):
                print("AI1 wins this round!")
                ai_points1 += 1
            else:
                print("AI2 wins this round!")
                ai_points2 += 1

            rounds_played += 1
            print(f"Round {rounds_played}/{user_rounds} completed.")
            print(f"Current score -> AI1: {ai_points1}, AI2: {ai_points2}\n")

        # Final result after all rounds
        if ai_points1 > ai_points2:
            print(f"AI1 wins the game! Final score -> AI1: {ai_points1}, AI2: {ai_points2}")
        elif ai_points1 < ai_points2:
            print(f"AI2 wins the game! Final score -> AI1: {ai_points1}, AI2: {ai_points2}")
        else:
            print(f"The game is a tie! Final score -> AI1: {ai_points1}, AI2: {ai_points2}")

play_game()