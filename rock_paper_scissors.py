import random

user_points = 0
ai_points = 0

try:
    user_rounds = int(input("Enter the number of rounds you want to play: "))
except ValueError:
    print("Please enter a valid number of rounds, only a number not a decimal to.")

while True:
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    except ValueError:
        print("Please enter a valid choice.")

    ai_choise = random.randint(1, 1)

    choice = {
        1: "rock",
        2: "paper",
        3: "scissors"
    }

    if user_input == choice[ai_choise]:
        print("It's a tie!")
        user_points -= 1
        ai_points -= 1
        print(f"User points: {user_points} and AI points: {ai_points}")
    elif user_input == "rock" and choice[ai_choise] == "scissors":
        print("You win!")
        user_points += 1
    elif user_input == "paper" and choice[ai_choise] == "rock":
        print("You win!")
        user_points += 1
    elif user_input == "scissors" and choice[ai_choise] == "paper":
        print("you win!")
        user_points += 1
    else:
        print("You lose!")
        ai_points += 1
    
    if user_points == user_rounds and ai_points == user_rounds:
        print("It's a tie!")
        break
    elif user_points == user_rounds:
        print("You win the game!")
        break
    else:
        print("AI wins the game!")
        break