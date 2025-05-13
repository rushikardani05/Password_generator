import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_specials = specials_var.get()

        characters = string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_specials:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")



# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")
window.resizable(False, False)

# Input: Password length
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.insert(0, "12")  # Default length
length_entry.pack()

# Checkboxes for options
digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(window, text="Include Special Characters", variable=specials_var).pack()

# Button to generate password
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

# Label to show result
result_label = tk.Label(window, text="", font=("Courier", 12), fg="green")
result_label.pack()

# Start GUI loop
window.mainloop()
