import tkinter as tk
import random

# Global variable to track the current player's turn
current_player = 1

def roll_dice():
    global current_player
    
    try:
        # Get the number of players and rolls
        num_players = int(entry_players.get())
        rolls = int(entry_rolls.get())  # Get the number of rolls
        dice = int(entry_dice.get())  # Get the number of sides on the dice
        player_turn = entry_player_turn.get().strip().lower()  # Get the player's turn input
        
        # Clear previous results
        result_text.delete(1.0, tk.END)
        
        # Validate inputs
        if rolls <= 0 or dice <= 0 or num_players <= 0:
            result_text.insert(tk.END, "Please enter valid numbers for the number of players, rolls, and dice sides.\n")
            return
        
        # Check if it's the right player's turn
        if player_turn == f'player{current_player}':  # Check if the input matches the current player's turn
            results = []
            for _ in range(rolls):
                number = random.randint(1, dice)
                results.append(f"Player {current_player} rolled: {number}")
            
            # Display the current player's result
            result_text.insert(tk.END, "\n".join(results) + "\n")
            result_text.yview(tk.FIRST)  # Scroll to the top after the roll
            
            # Move to the next player's turn
            current_player += 1
            if current_player > num_players:
                result_text.insert(tk.END, "\nAll players have rolled!\n")
                roll_button.config(state=tk.DISABLED)  # Disable the button after everyone has rolled
        else:
            result_text.insert(tk.END, f"It's not Player {current_player}'s turn. Please input the correct player's turn.\n")
        
    except ValueError:
        result_text.insert(tk.END, "Please use numbers for all inputs.\n")
        result_text.yview(tk.FIRST)  # Scroll to the top after error

def reset_game():
    global current_player
    
    # Reset the game state
    current_player = 1
    result_text.delete(1.0, tk.END)
    roll_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Multi-Player Dice Roller")

# Create labels and entry fields
label_players = tk.Label(window, text="Enter the number of players:")
label_players.pack()

entry_players = tk.Entry(window)
entry_players.pack()

label_rolls = tk.Label(window, text="How many times do you want each player to roll?")
label_rolls.pack()

entry_rolls = tk.Entry(window)
entry_rolls.pack()

label_dice = tk.Label(window, text="Enter the number that you want the dice to be out of:")
label_dice.pack()

entry_dice = tk.Entry(window)
entry_dice.pack()

label_player_turn = tk.Label(window, text="Enter the player's turn (e.g., player1, player2):")
label_player_turn.pack()

entry_player_turn = tk.Entry(window)
entry_player_turn.pack()

# Create a button to trigger the dice rolling
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Create a button to reset the game
reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack()

# Create a canvas and scrollbar for results
result_frame = tk.Frame(window)
result_frame.pack()

canvas = tk.Canvas(result_frame)
scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a text widget inside the canvas for results
result_text = tk.Text(canvas, height=10, width=50)
canvas.create_window((0, 0), window=result_text, anchor="nw")

# Update scroll region when the content is updated
result_text.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

# Run the application
window.mainloop()
