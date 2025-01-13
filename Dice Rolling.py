import tkinter as tk
import random

def roll_dice():
    try:
        # Get the number of players
        num_players = int(entry_players.get())
        
        # Clear previous results
        result_text.delete(1.0, tk.END)

        # Roll for each player
        for player in range(1, num_players + 1):
            rolls = int(entry_rolls.get())  # Get the number of rolls
            dice = int(entry_dice.get())  # Get the number of sides on the dice

            # Validate the inputs
            if rolls <= 0 or dice <= 0:
                result_text.insert(tk.END, f"Please enter valid numbers for player {player}.\n")
                break
            else:
                results = []
                for _ in range(rolls):
                    number = random.randint(1, dice)
                    results.append(f"Player {player} rolled: {number}")
                
                # Display each player's result
                result_text.insert(tk.END, "\n".join(results) + "\n")
        result_text.yview(tk.END)  # Scroll to the bottom after each roll
    except ValueError:
        result_text.insert(tk.END, "Please use numbers for all inputs.\n")
        result_text.yview(tk.END)  # Scroll to the bottom after error

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

# Create a button to trigger the dice rolling
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack()

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
