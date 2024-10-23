import tkinter as tk
from tkinter import messagebox

# Function for calculation logic
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Setting up the GUI
app = tk.Tk()
app.title("Simple Calculator")

# Create entry fields for numbers
tk.Label(app, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Create radio buttons for operation selection
operation_var = tk.StringVar(value='add')

tk.Label(app, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(app, text="Addition", variable=operation_var, value='add').grid(row=2, column=1)
tk.Radiobutton(app, text="Subtraction", variable=operation_var, value='sub').grid(row=3, column=1)
tk.Radiobutton(app, text="Multiplication", variable=operation_var, value='mul').grid(row=4, column=1)
tk.Radiobutton(app, text="Division", variable=operation_var, value='div').grid(row=5, column=1)

# Create a button to trigger the calculation
btn_calculate = tk.Button(app, text="Calculate", command=calculate)
btn_calculate.grid(row=6, column=1, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(app, text="Result: ", font=("Arial", 14))
label_result.grid(row=7, column=1, padx=10, pady=10)

# Start the GUI application
app.mainloop()
