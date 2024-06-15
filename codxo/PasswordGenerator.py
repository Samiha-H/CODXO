import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.generated_password = tk.StringVar()
        self.generated_password_entry = tk.Entry(master, textvariable=self.generated_password, state='readonly')
        self.generated_password_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        if length < 4:
            self.generated_password.set("Password length must be at least 4 characters.")
            return

        # Define the character sets for the password
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine the character sets
        all_characters = lowercase_letters + uppercase_letters + digits + symbols

        # Generate the password
        password = ''.join(random.sample(all_characters, length))
        self.generated_password.set(password)

def main():
    root = tk.Tk()
    generator = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
