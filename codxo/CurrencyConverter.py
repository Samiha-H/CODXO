import tkinter as tk
import json
from urllib.request import urlopen

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(master, text="From Currency:")
        self.from_currency_label.pack()

        self.from_currency_entry = tk.Entry(master)
        self.from_currency_entry.pack()

        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_entry = tk.Entry(master)
        self.to_currency_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = urlopen(url)
        data = json.loads(response.read().decode())
        conversion_rate = data['rates'][to_currency]

        converted_amount = amount * conversion_rate
        self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

def main():
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
