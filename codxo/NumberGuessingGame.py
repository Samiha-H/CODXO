import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)
        self.number_of_guesses = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.hint_label = tk.Label(root, text="")
        self.hint_label.pack()
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.number_of_guesses += 1
            
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low. Try again!")
                self.give_hint(guess)
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high. Try again!")
                self.give_hint(guess)
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.number_of_guesses} attempts.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
        
    def give_hint(self, guess):
        if self.number_to_guess % 2 == 0:
            parity_hint = "The number is even."
        else:
            parity_hint = "The number is odd."
        
        if self.number_to_guess % 3 == 0:
            multiple_of_3_hint = "The number is a multiple of 3."
        else:
            multiple_of_3_hint = "The number is not a multiple of 3."
        
        if abs(self.number_to_guess - guess) <= 10:
            proximity_hint = "You're very close!"
        else:
            proximity_hint = "You're far away."

        self.hint_label.config(text=f"Hints: {parity_hint} {multiple_of_3_hint} {proximity_hint}")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.number_of_guesses = 0
        self.result_label.config(text="")
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
