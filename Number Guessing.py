import random
import tkinter as tk
from tkinter import messagebox

class GuessGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        # Initialize variables
        self.num = None
        self.number = None
        self.players = []
        self.current_player = 1

        # Widgets
        self.label_prompt = tk.Label(root, text="Enter a number to guess out of (greater than 5):")
        self.label_prompt.pack(pady=5)

        self.entry_input = tk.Entry(root)
        self.entry_input.pack(pady=5)

        self.button_submit = tk.Button(root, text="Submit", command=self.get_max_number)
        self.button_submit.pack(pady=5)

        self.label_feedback = tk.Label(root, text="")
        self.label_feedback.pack(pady=5)

    def get_max_number(self):
        try:
            value = int(self.entry_input.get())
            if value <= 5:
                self.label_feedback.config(text="Please enter a number greater than 5.")
            else:
                self.num = value
                self.number = random.randint(1, self.num)
                self.entry_input.delete(0, tk.END)
                self.label_prompt.config(text=f"Player {self.current_player}, enter your guess (1 to {self.num}):")
                self.button_submit.config(command=self.get_player_guess)
                self.label_feedback.config(text="")
        except ValueError:
            self.label_feedback.config(text="Invalid input. Please enter a valid number.")

    def get_player_guess(self):
        try:
            guess = int(self.entry_input.get())
            if guess < 1 or guess > self.num:
                self.label_feedback.config(text=f"Please enter a number between 1 and {self.num}.")
            else:
                self.players.append(guess)
                self.entry_input.delete(0, tk.END)
                if self.current_player < 4:
                    self.current_player += 1
                    self.label_prompt.config(text=f"Player {self.current_player}, enter your guess (1 to {self.num}):")
                else:
                    self.check_winners()
        except ValueError:
            self.label_feedback.config(text="Invalid input. Please enter a valid number.")

    def check_winners(self):
        winners = [f"Player {i+1}" for i, guess in enumerate(self.players) if guess == self.number]
        if winners:
            if len(winners) == 4:
                messagebox.showinfo("Result", "You all win!")
            else:
                messagebox.showinfo("Result", ", ".join(winners) + " win(s)!")
        else:
            messagebox.showinfo("Result", f"Sorry, no one wins. The number was {self.number}.")
        self.reset_game()

    def reset_game(self):
        self.num = None
        self.number = None
        self.players = []
        self.current_player = 1
        self.label_prompt.config(text="Enter a number to guess out of (greater than 5):")
        self.entry_input.delete(0, tk.END)
        self.button_submit.config(command=self.get_max_number)
        self.label_feedback.config(text="")
# Run the application
root = tk.Tk()
app = GuessGameApp(root)
root.mainloop()