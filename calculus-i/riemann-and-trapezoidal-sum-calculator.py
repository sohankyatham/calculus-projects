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


# FUNCTIONS

# Plot sum approximation - plots the graph of f(x) and draws the shapes (representing sum approximation) to visualize the integral
def plot_sum_approximation(x_values, fx_values, approximation_type):
    plt.clf()
    plt.plot(x_values, fx_values, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')

    # Plot rectangles or trapezoids based on the selected approximation type
    if approximation_type == "left_riemann":
        for i in range(len(x_values) - 1):
            # Fill the area under the function curve with rectangles
            plt.fill_between([x_values[i], x_values[i+1]], [fx_values[i], fx_values[i]], alpha=0.3)
    elif approximation_type == "right_riemann":
        for i in range(1, len(x_values)):
            # Fill the area under the function curve with rectangles
            plt.fill_between([x_values[i-1], x_values[i]], [fx_values[i], fx_values[i]], alpha=0.3)
    elif approximation_type == "trapezoidal_sum":
        for i in range(len(x_values) - 1):
            # Fill the area under the function curve with trapezoids
            plt.fill_between([x_values[i], x_values[i+1]], [fx_values[i], fx_values[i+1]], alpha=0.3)

    # Display the legend and show the plot
    plt.legend()
    plt.show()

# Calculate sum - performs the calculation using the desired approximation type
def calculate_sum(x_values, fx_values):
    total_sum = 0
    approximation_type = radio_var.get()

    # Left Riemann Sum
    if approximation_type == "left_riemann":
        for i in range(len(x_values) - 1):
            width = (x_values[i + 1] - x_values[i])
            height = fx_values[i]
            total_sum += (width * height)

    # Right Riemann Sum
    elif approximation_type == "right_riemann":
        for i in range(len(x_values) - 1):
            base = (x_values[i + 1] - x_values[i])
            height = fx_values[i + 1]
            total_sum += (base * height)

    # Trapezoidal Sum: Area = 0.5 * (f(x_i) + f(x_{i+1})) * Δx
    elif approximation_type == "trapezoidal_sum":
        for i in range(len(x_values) - 1):
            height = (x_values[i + 1] - x_values[i])
            base_1 = fx_values[i] 
            base_2 = fx_values[i + 1] 
            total_sum += 0.5 * (base_1 + base_2) * height
    
    # Update the total_sum_label to display the sum of the area 
    total_sum_label.config(text="Sum of Area: " + str(total_sum))

    # Call plot_sum_approximation to graph the points and shapes under the curve depicting area
    plot_sum_approximation(x_values, fx_values, approximation_type)

# Initializes calculation - prepares the calculation by extracting x and f(x) values from user input
def initialize_calculation():
    try:
        x_values = [float(x) for x in x_values_entry.get().split()]
        fx_values = [float(x) for x in function_values_entry.get().split()]

        # Check if the user enters the same number of values for x and f(x)
        if len(x_values) < 2:
            messagebox.showerror("Error", "At least two data points are required.")
            return
        else:
            if len(x_values) == len(fx_values):
                    calculate_sum(x_values, fx_values)
            else:
                # Display error message if the number of x and f(x) values are different
                messagebox.showerror("Error", "The number of x and f(x) values must be equal")
                return

    except ValueError:
        # Display error if the values of x and/or f(x) are not numerical
        messagebox.showerror("Error", "Values of x and f(x) must be numerical")

# Function to export the graph as an image file
def export_graph(*args):
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if filename:
        plt.savefig(filename)
        tk.messagebox.showinfo("Export Successful", "Graph has been exported successfully.")
# Bind export_canvas with the keyboard binding Ctrl+s
root.bind('<Control-Key-s>', export_graph)

# Function to clear the entered data and graph
def clear_canvas(*args):
    # Clear the Entry fields for x and f(x) values
    x_values_entry.delete(0, tk.END)
    function_values_entry.delete(0, tk.END)
    plt.clf()
    plt.close("all")
    tk.messagebox.showinfo("Data Cleared", "Entered data and graph have been cleared.")
# Bind clear_canvas with the keyboard binding Ctrl+l
root.bind('<Control-Key-l>', clear_canvas)

# Exits the program
def exit_func(*args):
    root.destroy()


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

# Entry for Entering f(x) values
function_values_entry = tk.Entry(root, width=50)
function_values_entry.pack(pady=5)

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
right_riemann_radio.pack(anchor=tk.W)

# Radio button for trapezoidal sum
trapezoidal_sum_radio = tk.Radiobutton(radio_btns_frame, text="Trapezoidal Sum", variable=radio_var, value="trapezoidal_sum")
trapezoidal_sum_radio.pack(anchor=tk.W)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate", width=16, font=("Arial", 11), bg="#26aceb", command=initialize_calculation)
calculate_btn.pack(pady=10)

# Total sum label
total_sum_label = tk.Label(root, text="Sum of Area: ...", font=("Arial", 11))
total_sum_label.pack(pady=15)

# Menu Bar for menu options on top of window
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu - graph options for clearing, saving graph, & exiting program
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Graph as Image", accelerator="Ctrl+s", command=export_graph)
file_menu.add_command(label="Clear", accelerator="Ctrl+l", command=clear_canvas)
file_menu.add_separator()
file_menu.add_command(label="Exit Window", accelerator="Alt-F4", command=exit_func)

root.mainloop()