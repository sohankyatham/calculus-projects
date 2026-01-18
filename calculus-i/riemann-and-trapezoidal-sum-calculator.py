# Riemann & Trapezoidal Sum Calculator with Python 
# This program estimates the area under a curve using numerical integration methods such as Riemann Sums (LRAM & RRAM) or the Trapezoidal Rule 

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt

# Create tkinter window
root = tk.Tk()
root.title("Riemann & Trapezoidal Sum Calculator")
root.geometry("400x400")


# USER INTERFACE

# Label for entering x-values
x_value_label = tk.Label(root, text="Enter values of x:", font=("Arial", 11))
x_value_label.pack(pady=5)

# Entry for entering x-values
x_values_entry = tk.Entry(root, width=50)

root.mainloop()