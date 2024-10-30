class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store:
    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print("Menu:")
        for key, value in self.menu.items():
            print(f"{key}: {value.name:15} : {value.price} Rs. ")


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item, quantity):
        total_cost = item.price * quantity
        self.cart.append({"name": item.name, "quantity": quantity, "total_cost": total_cost})
        print(f"Added {quantity} x {item.name} to your cart.")

    def display_cart(self):
        if self.cart:
            print("\n--------------\n  Your Cart\n--------------")
            for item in self.cart:
                print(f"{item['quantity']} x {item['name']}")
        else:
            print("Your cart is empty.")

    def calculate_total_bill(self):
        total_bill = sum(item["total_cost"] for item in self.cart)
        print(f"\n--------------\n  Total Bill\n--------------\n  {total_bill:.2f} Rs. ")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username and password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    menu_items = {
        "0": MenuItem("Sugar", 60.00),
        "1": MenuItem("Flour", 50.00),
        "2": MenuItem("Cereal", 40.00),
        "3": MenuItem("Milk", 30.00),
        "4": MenuItem("Cookies", 35.00),
        "5": MenuItem("Candy", 15.00),
        "6": MenuItem("Rice", 50.00),
        "7": MenuItem("Cake", 60.00),
        "8": MenuItem("Cold Drinks", 20.00),
        "9": MenuItem("Chips", 20.00),
    }

    store = Store(menu_items)
    cart = ShoppingCart()

    login()

    store.display_menu()

    while True:
        selection = input(
            "\nPlease select an item (1-10), 'C' for cart, 'B' for bill, or 'q' to exit: "
        ).lower()

        if selection == "q":
            break
        elif selection in menu_items:
            item = menu_items[selection]
            print(f"You have selected: {item.name}")
            quantity = int(input("How many would you like? "))
            cart.add_to_cart(item, quantity)
        elif selection == "c":
            cart.display_cart()
        elif selection == "b":
            cart.calculate_total_bill()
        else:
            print("Invalid selection. Please choose a valid option.")


if __name__ == "__main__":
    main()
