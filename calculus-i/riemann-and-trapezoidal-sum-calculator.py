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
x_values_entry.pack(pady=5)

# Label for entering f(x) values
function_value_label = tk.Label(root, text="Enter values for f(x):", font=("Arial", 11))
function_value_label.pack(pady=5)

# Frame for storing radio buttons
radio_btns_frame = tk.Frame(root)
radio_btns_frame.pack(pady=10)

# Label for selecting approximation type
approximation_type_label = tk.Label(radio_btns_frame, text="Select Approximation Type:", font=("Arial", 11))
approximation_type_label.pack()

# radio_var for helping select the radio buttons and getting the value; default is left riemann sum
radio_var = tk.StringVar(value="left_riemann")

# Radio button for left riemann sum
left_riemann_radio = tk.Radiobutton(radio_btns_frame, text="Left Riemann Sum (LRAM)", variable=radio_var, value="left_riemann")
left_riemann_radio.pack(anchor=tk.W)

# Radio button for right riemann sum
right_riemann_radio = tk.Radiobutton(radio_btns_frame, text="Right Riemann Sum (RRAM)", variable=radio_var, value="right_riemann")

root.mainloop()