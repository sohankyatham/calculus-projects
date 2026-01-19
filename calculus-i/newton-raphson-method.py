# Newton-Raphson Method with Python
# This program calculates the approximate square root of a number using the Newton-Raphson method

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser


# Create a tkinter window 
root = tk.Tk()
root.title("Newton-Raphson Method with Python")
root.geometry("600x600")


# Function used to check if user entered valid number & assigns variables to calculate sqrt using newtons method
def calculate_sqrt():
    clear_canvas()
    # Make sure that the user enters a positive number (cant be negative or equal to 0), display error on result_label otherwise
    try:
        number = float(number_entry.get())
        if (number < 0):
            result_label.config(text="Please enter a non-negative number")
        elif (number == 0):
            result_label.config(text="Please enter a number greater than 0")
        else:
            clear_canvas()
            # If the user entered a valid number, call the newton_raphson_method function to evaluate the square root
            newton_raphson_method(number)
    
    # Make sure the user doesn't enter invalid arguments such as a string or symbols
    except ValueError: 
        result_label.config(text="Invalid input. Please enter a number")


# This function calculates the square root using the newton-raphson method
def newton_raphson_method(number, max_decimal_points=1e-9, delay=1000):
    # Initial guess - half the number:
    x = number / 2
    # Number of iterations of newton-raphson's method
    iteration += 1

    # Function to calculate sqrt and update the text in result_label
    def update_label(x, iteration):
        # Calculate the next approximation of the square root using the newton-raphson method iteration
        x_of_n = x - ((x * x - number) / (2 * x))

        # Check if the difference between the current and next approximation is within the desired precision
        if abs(x_of_n - x) < max_decimal_points:
            result_label.config(text=f"The square root of {number} is approximately {x_of_n:.9f} (after {iteration} iterations)")
            iteration = 0
        else:
            result_label.config(text=f"Iteration {iteration + 1}: {x_of_n:.9f}")
            root.after(delay, update_label, x_of_n, iteration + 1) 
            update_graph(x_of_n)
    
    update_label(x, iteration)
   

# Update the graph to show the root approximation vs. the iteration number 
def update_graph(root_approximation):
    roots.append(root_approximation)
    
    # Clear the previous plot on the axis
    ax.clear()
    
    # Plot the root approximations against their indices
    ax.plot(range(len(roots)), roots, marker='o', color='blue')

    # Plot a horizontal line at y=0 to represent the x-axis
    ax.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
    
    # Set labels for the x and y axes
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Root Approximation')
    
    # Redraw the canvas to reflect the updated plot
    canvas.draw()

'''
Menu Functions
'''
# Clears the graph and its contents on the canvas
def clear_canvas(*args):
    global roots
    # Clear the roots list
    roots = []
    # Clear the axis of all plots
    ax.clear()
    # Redraw the canvas
    canvas.draw()
# Bind clear_canvas with the keyboard binding Ctrl+l
root.bind('<Control-Key-l>', clear_canvas)


# Saves the contents of the graph on the canvas as an image file
def save_graph_as_image(*args):
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")])
    if filename:
        fig.savefig(filename)
root.bind('<Control-Key-s>', save_graph_as_image)


# Exits the program
def exit_func(*args):
    root.destroy()
# Bind exit_func with the keyboard binding of Alt-F4
root.bind("<Alt-Key-F4>", exit_func)


# Opens link to Project Repository
def view_project():
    webbrowser.open("https://github.com/sohankyatham/Newton-Raphson-Method-with-Python")


# Opens new TopLevel window about the program
def about_screen():
    # about_screen_window
    about_screen_window = tk.Toplevel(root)
    about_screen_window.title("About")
    about_screen_window.geometry("400x200")
    about_screen_window.resizable(0,0)

    # about_header - Displays a Label called "Square Root Calculator Using Newton's Method"
    about_header = tk.Label(about_screen_window, text="Newton-Raphson Method with Python", font=("Arial", 14))
    about_header.pack(pady=5)

    # description - Displays a brief description for project
    description = tk.Label(about_screen_window, text="A square root approximation calculator using Newton-Raphson Method \n Made in python")
    description.pack()

    # header_attribtion - Shows that I created the program
    header_attribtion = tk.Label(about_screen_window, text="By: Sohan Kyatham", width=16, font=("Arial", 12))
    header_attribtion.pack()

    # about_version - Displays the version of the program
    about_version = tk.Label(about_screen_window, text="Version: 1.0.0", width=16, font=("Arial", 12))
    about_version.pack()

    # view_project_repository - View Project Repository Button
    view_project_repository = tk.Button(about_screen_window, text="View Project Repository", width=26, font=("Arial", 12), bg="#26aceb", command=view_project)
    view_project_repository.pack(pady=15)

    # Mainloop for about_screen_window
    about_screen_window.mainloop()


# Create Number Input Label
number_entry_label = tk.Label(root, font=("Arial", 11), text="Enter a number to find the square root approximation: ")
number_entry_label.pack()

# Create Number Input Entry Field
number_entry = tk.Entry(root)
number_entry.pack()

# Calculate Button
calculate_btn = tk.Button(root, text="Calculate", width=16, font=("Arial", 11), bg="#26aceb", command=calculate_sqrt)
calculate_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Create a Matplotlib Figure
fig, ax = plt.subplots()

# Create a canvas compatible with tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# List to store root approximations for plotting
roots = []


# menu_bar - Place for Placing Menu Options
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# file_menu - Graph options for clearing & saving graph + exiting program
file_menu = tk.Menu(menu_bar, tearoff=False)
# Add the graph_menu to the menu_bar
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear Graph", accelerator="Ctrl+l", command=clear_canvas)
file_menu.add_command(label="Save Graph as Image", accelerator="Ctrl+s", command=save_graph_as_image)
file_menu.add_separator()
file_menu.add_command(label="Exit Window", accelerator="Alt-F4", command=exit_func)

# help_menu - About & Documentation
help_menu = tk.Menu(menu_bar, tearoff=False)
# Add the about_menu to the menu_bar
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="View Project Repository", command=view_project)
help_menu.add_command(label="About", command=about_screen)


root.mainloop()