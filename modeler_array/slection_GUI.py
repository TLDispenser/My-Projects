import tkinter as tk
from tkinter import messagebox

from models import MODLES


class SelectionUI:
    def __init__(self, root):
        self.root = root
        self.main_screen()
        self.root.title("Selection GUI")
        tk.Label(self.root, text="Select a model").pack()
        for model in MODLES:
            tk.Button(self.root, text=model, command=lambda m=model: self.select_model(m)).pack()

    # Clear the current screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()      
            
    def main_screen(self):
        self.clear_screen()

        self.root.title("Main Screen")
        tk.Label(self.root, text="Welcome to the main screen!").pack(pady=10)
        tk.Button(self.root, text="Select Model", command=self.select_model_screen).pack(pady=5)

    def select_model(self, model):
        # Send the data out (you can replace this with actual data sending logic)
        print(f"Model selected: {model}")
        # Switch to the edit mode screen
        self.edit_mode_screen()

    def edit_mode_screen(self):
        self.clear_screen()

        self.root.title("Edit Mode Sclection")
        tk.Label(self.root, text="Do you want to enter edit mode?").pack(pady=10)

        tk.Button(self.root, text="Yes", command=self.enter_edit_mode).pack(pady=5)
        tk.Button(self.root, text="No", command=self.exit_edit_mode).pack(pady=5)

    def enter_edit_mode(self):
        messagebox.showinfo("Edit Mode", "Entering edit mode...")
        self.main_screen()

    def exit_edit_mode(self):
        messagebox.showinfo("Edit Mode", "Exiting edit mode...")
        self.main_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = SelectionUI(root)
    root.mainloop()
