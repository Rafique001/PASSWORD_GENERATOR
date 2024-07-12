import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from password_generator import PasswordGenerator

class PasswordGeneratorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.length_label = ttk.Label(self.main_frame, text="Password Length:")
        self.length_label.grid(column=0, row=0, sticky=tk.W, pady=5)

        self.length_entry = ttk.Entry(self.main_frame)
        self.length_entry.grid(column=1, row=0, pady=5)

        self.generate_button = ttk.Button(self.main_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=1, row=1, pady=5)

        self.password_label = ttk.Label(self.main_frame, text="Generated Password:")
        self.password_label.grid(column=0, row=2, sticky=tk.W, pady=5)

        self.password_display = ttk.Entry(self.main_frame, state='readonly')
        self.password_display.grid(column=1, row=2, pady=5)

        self.copy_button = ttk.Button(self.main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(column=1, row=3, pady=5)

        self.strength_label = ttk.Label(self.main_frame, text="Password Strength:")
        self.strength_label.grid(column=0, row=4, sticky=tk.W, pady=5)

        self.strength_display = ttk.Label(self.main_frame, text="")
        self.strength_display.grid(column=1, row=4, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")

            password_generator = PasswordGenerator(length)
            password = password_generator.generate()
            strength = password_generator.evaluate_strength(password)

            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')

            self.strength_display.config(text=strength)
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Empty", "No password to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorUI(root)
    root.mainloop()
