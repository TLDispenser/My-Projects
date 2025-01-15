import tkinter as tk
from tkinter import messagebox

from model import MODLES


class SelectionUI:
    def __init__(self, root):
        self.root = root
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
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Vertex", command=self.add_vertex).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Remove Vertex", command=self.remove_vertex).grid(row=0, column=1, padx=5)
        
        tk.Button(button_frame, text="Add Edge", command=self.add_edge).grid(row=1, column=0, padx=5)
        tk.Button(button_frame, text="Remove Edge", command=self.remove_edge).grid(row=1, column=1, padx=5)
        
        tk.Button(button_frame, text="Add Face", command=self.add_face).grid(row=2, column=0, padx=5)
        tk.Button(button_frame, text="Remove Face", command=self.remove_face).grid(row=2, column=1, padx=5)
        
        tk.Button(button_frame, text="Set Pivot Point", command=self.set_pivot_point).grid(row=3, column=0, padx=5)
        
        tk.Button(button_frame, text="Turn Edge Shows On/Off", command=self.toggle_edge_shows).grid(row=4, column=0, columnspan=2, pady=5)
        
        tk.Button(button_frame, text="Move Vertex", command=self.move_vertex).grid(row=5, column=0, columnspan=2, pady=5)

    def add_vertex(self):
        print("Add Vertex")

    def remove_vertex(self):
        print("Remove Vertex")

    def add_edge(self):
        print("Add Edge")

    def remove_edge(self):
        print("Remove Edge")

    def add_face(self):
        print("Add Face")

    def remove_face(self):
        print("Remove Face")

    def set_pivot_point(self):
        print("Set Pivot Point")

    def toggle_edge_shows(self):
        print("Toggle Edge Shows On/Off")

    def move_vertex(self):
        print("Move Vertex")
        
        
        
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
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SelectionUI(root)
    root.mainloop()
