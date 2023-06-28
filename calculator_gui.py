import tkinter as tk
from tkinter import messagebox

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = int(option_var.get())

        if choice == 1:
            result = addition(num1, num2)
            operation = "Addition"
        elif choice == 2:
            result = subtraction(num1, num2)
            operation = "Subtraction"
        elif choice == 3:
            result = multiplication(num1, num2)
            operation = "Multiplication"
        elif choice == 4:
            try:
                result = division(num1, num2)
                operation = "Division"
            except ZeroDivisionError as e:
                messagebox.showerror("Error", str(e))
                return

        result_label.configure(text=f"The result of {operation.lower()} is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input fields and labels
label_num1 = tk.Label(window, text="First number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Second number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create operation options
option_var = tk.IntVar()
option_var.set(1)  # Default choice is Addition

label_operation = tk.Label(window, text="Select an operation:")
label_operation.pack()

addition_radio = tk.Radiobutton(window, text="Addition", variable=option_var, value=1)
addition_radio.pack()
subtraction_radio = tk.Radiobutton(window, text="Subtraction", variable=option_var, value=2)
subtraction_radio.pack()
multiplication_radio = tk.Radiobutton(window, text="Multiplication", variable=option_var, value=3)
multiplication_radio.pack()
division_radio = tk.Radiobutton(window, text="Division", variable=option_var, value=4)
division_radio.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
