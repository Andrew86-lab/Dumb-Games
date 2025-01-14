import tkinter as tk
import random

def check_guesses():
    try:
        guesses = [int(entry.get()) for entry in entries]
        winner = next((f"🎉 Wow, Player {i+1}! You got it! The number was {number}" 
                       for i, guess in enumerate(guesses) if guess == number), 
                      f"😞 No one guessed it. The number was {number}")
        result_label.config(text=winner)
    except ValueError:
        result_label.config(text="Please enter valid numbers for all players.")

root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")

number = random.randint(1, 100)

tk.Label(root, text="Enter a number between 1 and 100:").pack(pady=10)

entries = []
for i in range(3):
    tk.Label(root, text=f"Player {i+1}:").pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

tk.Button(root, text="Submit Guesses", command=check_guesses).pack(pady=20)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()