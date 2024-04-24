import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")

# Create labels and entry fields
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create login button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()







import tkinter as tk

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + number)

def button_clear():
    entry_display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry field
entry_display = tk.Entry(root, width=20, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda text=text: button_click(text))
    button.grid(row=row, column=col)

# Run the Tkinter event loop
root.mainloop()
