import tkinter as tk
from tkinter import messagebox

class Restaurant:
    def __init__(self, name):
        self.name = name

class Admin:
    def __init__(self):
        self.items_list = []

    def login(self, username, password):
        return username == "admin" and password == "admin"

    def add_item(self, recipe, price):
        self.items_list.append({"recipe": recipe, "price": price})
        messagebox.showinfo("Success", f"Item '{recipe}' added successfully!")

    def delete_item(self, recipe):
        for item in self.items_list:
            if item["recipe"] == recipe:
                self.items_list.remove(item)
                messagebox.showinfo("Success", f"Item '{recipe}' deleted successfully!")
                return
        messagebox.showerror("Error", f"Item '{recipe}' not found!")

class Customer:
    def __init__(self, shared_items_list):
        self.order_items = []
        self.items_list = shared_items_list

    def login(self, username, password):
        return username == "customer" and password == "customer"

    def add_order(self, item):
        self.order_items.append(item)
        messagebox.showinfo("Success", f"'{item['recipe']}' added to your order!")

    def calculate_bill(self):
        total_price = sum(item['price'] for item in self.order_items)
        return total_price

    def checkout(self):
        if not self.order_items:
            messagebox.showinfo("Info", "No items to checkout!")
            return

        total_price = self.calculate_bill()
        self.order_items.clear()
        messagebox.showinfo("Checkout", f"Thank you for your purchase! Total: ${total_price}")

class RestaurantApp:
    def __init__(self, root):
        self.restaurant = Restaurant("Boykot")
        self.shared_items_list = []
        self.admin = Admin()
        self.admin.items_list = self.shared_items_list
        self.customer = Customer(self.shared_items_list)

        self.root = root
        self.root.title(self.restaurant.name)
        self.root.geometry("500x500")

        self.main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text=f"Welcome to {self.restaurant.name}!", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Admin Login", command=self.admin_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Customer Login", command=self.customer_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20, font=("Arial", 14)).pack(pady=10)

    def admin_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Admin Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        username_entry = tk.Entry(self.root, font=("Arial", 14))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        password_entry.pack()

        def handle_login():
            if self.admin.login(username_entry.get(), password_entry.get()):
                self.admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        tk.Button(self.root, text="Login", command=handle_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def admin_dashboard(self):
        self.clear_frame()

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Add Item", command=self.add_item, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Delete Item", command=self.delete_item, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="View Items", command=self.view_items, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def add_item(self):
        self.clear_frame()

        tk.Label(self.root, text="Add Item", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Recipe Name:", font=("Arial", 14)).pack()
        recipe_entry = tk.Entry(self.root, font=("Arial", 14))
        recipe_entry.pack()

        tk.Label(self.root, text="Price:", font=("Arial", 14)).pack()
        price_entry = tk.Entry(self.root, font=("Arial", 14))
        price_entry.pack()

        def handle_add():
            recipe = recipe_entry.get()
            try:
                price = float(price_entry.get())
                self.admin.add_item(recipe, price)
                self.admin_dashboard()
            except ValueError:
                messagebox.showerror("Error", "Invalid price!")

        tk.Button(self.root, text="Add", command=handle_add, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack()

    def delete_item(self):
        self.clear_frame()

        tk.Label(self.root, text="Delete Item", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Recipe Name:", font=("Arial", 14)).pack()
        recipe_entry = tk.Entry(self.root, font=("Arial", 14))
        recipe_entry.pack()

        def handle_delete():
            recipe = recipe_entry.get()
            self.admin.delete_item(recipe)
            self.admin_dashboard()

        tk.Button(self.root, text="Delete", command=handle_delete, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack()

    def view_items(self):
        self.clear_frame()

        tk.Label(self.root, text="Items List", font=("Arial", 18)).pack(pady=20)

        for item in self.shared_items_list:
            tk.Label(self.root, text=f"{item['recipe']} - ${item['price']}", font=("Arial", 14)).pack()

        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack(pady=10)

    def customer_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Customer Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        username_entry = tk.Entry(self.root, font=("Arial", 14))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        password_entry.pack()

        def handle_login():
            if self.customer.login(username_entry.get(), password_entry.get()):
                self.customer_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        tk.Button(self.root, text="Login", command=handle_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def customer_dashboard(self):
        self.clear_frame()

        tk.Label(self.root, text="Customer Dashboard", font=("Arial", 18)).pack(pady=20)

        for item in self.shared_items_list:
            tk.Button(self.root, text=f"{item['recipe']} - ${item['price']}",
                      command=lambda i=item: self.customer.add_order(i),
                      width=30, font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="View Bill", command=self.view_bill, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Checkout", command=self.customer.checkout, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def view_bill(self):
        self.clear_frame()

        tk.Label(self.root, text="Your Bill", font=("Arial", 18)).pack(pady=20)

        total_price = 0
        for item in self.customer.order_items:
            tk.Label(self.root, text=f"{item['recipe']} - ${item['price']}", font=("Arial", 14)).pack()
            total_price += item['price']

        tk.Label(self.root, text=f"Total: ${total_price}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Back", command=self.customer_dashboard, width=20, font=("Arial", 14)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
