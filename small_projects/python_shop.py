# Description: This file contains the data for the shop in this program.

# Dictionary to store the items that are available to buy
avalble_to_buy = {
    'Class': 
        {
            'name': 'Class',
            'price': 1000,
            'stock': 10
        },
    'Function':
        {
            'name': 'Function',
            'price': 500,
            'stock': 20
        },
    'Variable':
        {
            'name': 'Variable',
            'price': 200,
            'stock': 30
        },
    'Comment':
        {
            'name': 'Comment',
            'price': 50,
            'stock': 50
        },
    'Dictionary':
        {
            'name': 'Dictionary',
            'price': 300,
            'stock': 25
        },
    'List':
        {
            'name': 'List',
            'price': 150,
            'stock': 40
        },
    'Tuple':
        {
            'name': 'Tuple',
            'price': 250,
            'stock': 35
        },
    'String':
        {
            'name': 'String',
            'price': 100,
            'stock': 45
        },
    'Integer':
        {
            'name': 'Integer',
            'price': 50,
            'stock': 55
        },
    'Float':
        {
            'name': 'Float',
            'price': 75,
            'stock': 50
        },
    'Boolean':
        {
            'name': 'Boolean',
            'price': 25,
            'stock': 60
        },
    'While Loop':
        {
            'name': 'While Loop',
            'price': 150,
            'stock': 40
        },
    'For Loop':
        {
            'name': 'For Loop',
            'price': 200,
            'stock': 30
        },
    'If Statement':
        {
            'name': 'If Statement',
            'price': 100,
            'stock': 45
        },
    'Else Statement':
        {
            'name': 'Else Statement',
            'price': 75,
            'stock': 50
        },
    'Elif Statement':
        {
            'name': 'Elif Statement',
            'price': 125,
            'stock': 45
        },
    'Try Except':
        {
            'name': 'Try Except',
            'price': 200,
            'stock': 30
        },
    'Import':
        {
            'name': 'Import',
            'price': 50,
            'stock': 55
        },
    'Return':
        {
            'name': 'Return',
            'price': 100,
            'stock': 45
        },
    'Break':
        {
            'name': 'Break',
            'price': 75,
            'stock': 50
        },  
    'Continue':
        {
            'name': 'Continue',
            'price': 75,
            'stock': 50
        }
}
# Importing tkinter and messagebox to display the GUI
import tkinter as tk
from tkinter import messagebox


# Class to display the shop GUI so multiple instances can be created if need to be
class ShopGUI:
    
    def __init__(self, root):
        messagebox.showinfo("Welcome", "Welcome to the shop!")
        self.root = root
        self.main_screen()
        self.root.title("Shop")
        # Class global variable to store the total
        self.total = 0

        
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    # Screen to display the what the user can buy
    def main_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select an item to buy").pack()
        for item in avalble_to_buy:
            if avalble_to_buy[item]['stock'] > 0:
                tk.Button(self.root, text=item, command=lambda i=item: self.buy_item(i)).pack()
        tk.Label(self.root, text="").pack()  # Add an empty label for indentation
        tk.Button(self.root, text="Exit", command=self.exit).pack()
    # Buy item
    def buy_item(self, item):
        self.clear_screen()
        try:
            # Check if the item is in stock and display the price and stock
            if avalble_to_buy[item]['stock'] > 0:
                tk.Label(self.root, text=f"How many {item}s would you like to buy?").pack()
                tk.Label(self.root, text=f"Price: ${avalble_to_buy[item]['price']} each").pack()
                tk.Label(self.root, text=f"Ammount in stock: {avalble_to_buy[item]['stock']}").pack()
                quantity_var = tk.IntVar(value=1)
                tk.Spinbox(self.root, from_=0, to=avalble_to_buy[item]['stock'], textvariable=quantity_var).pack()
                tk.Button(self.root, text="Purchase", command=lambda: self.confirm_purchase(item, quantity_var.get())).pack()
            else:
                messagebox.showwarning("Out of Stock", f"Sorry, {item} is out of stock.")
                self.main_screen()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            self.buy_item(item)
    # Confirm purchase and update the stock and total
    def confirm_purchase(self, item, quantity):
        # If user types insteads of scrolls for quantity it will check if the quantity is in stock in there slected ammount
        if avalble_to_buy[item]['stock'] < quantity:
            messagebox.showwarning("Insufficient Stock", "There is not enough stock for that quantity.")
            self.clear_screen()
            self.buy_item(item)
        else:
            if messagebox.askyesno("Confirm Purchase", f"Are you sure you want to buy {quantity} {item}s?\nIn total it will cost you ${avalble_to_buy[item]['price'] * quantity}."):
                avalble_to_buy[item]['stock'] -= quantity
                self.total += avalble_to_buy[item]['price'] * quantity
                messagebox.showinfo("Purchase Successful", f"You have bought {quantity} {item}s.")
            self.main_screen()
    # Exit
    def exit(self):
        messagebox.showinfo("Total", f"Your total is ${self.total}.")
        messagebox.showinfo("Thank You", "Thank you for shopping!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShopGUI(root)
    root.mainloop()
