import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return f"Your Account Balance is ${self.balance}"

    def deposite(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Your New Balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. Your New Balance is ${self.balance}"
        else:
            return "Insufficient funds. Withdraw failed."


# Create an instance of the ATM class
atm = ATM()

# Function to handle checking balance
def check_balance():
    result = atm.check_balance()
    messagebox.showinfo("Balance", result)

# Function to handle deposit
def deposite():
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            result = atm.deposite(amount)
            messagebox.showinfo("Deposit", result)
            entry_amount.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to handle withdraw
def withdraw():
    try:
        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            result = atm.withdraw(amount)
            messagebox.showinfo("Withdraw", result)
            entry_amount.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to handle exit
def exit_atm():
    window.quit()

# Create the main window
window = tk.Tk()
window.title("ATM Machine")
window.geometry("400x300")

# Create and place labels and buttons
label_title = tk.Label(window, text="Welcome to the ATM", font=("Helvetica", 16))
label_title.pack(pady=10)

label_amount = tk.Label(window, text="Enter Amount:")
label_amount.pack()

entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

# Buttons for ATM functionalities
button_check_balance = tk.Button(window, text="Check Balance", width=20, command=check_balance)
button_check_balance.pack(pady=5)

button_deposite = tk.Button(window, text="Deposit", width=20, command=deposite)
button_deposite.pack(pady=5)

button_withdraw = tk.Button(window, text="Withdraw", width=20, command=withdraw)
button_withdraw.pack(pady=5)

button_exit = tk.Button(window, text="Exit", width=20, command=exit_atm)
button_exit.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
