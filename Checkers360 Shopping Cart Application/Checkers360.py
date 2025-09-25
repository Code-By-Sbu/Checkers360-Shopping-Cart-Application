def add_item(cart):
    item = input("Enter the item name: ").capitalize()
    try:
        price = float(input(f"Enter the price of {item}: R"))
        quantity = int(input(f"Enter the quantity of {item}: "))
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be an integer.")
        return

    if item in cart:
        cart[item]['quantity'] += quantity
        print(f"Updated {item}: New quantity = {cart[item]['quantity']}")
    else:
        cart[item] = {'price': price, 'quantity': quantity}
        print(f"{quantity} x {item}(s) added to the cart.")


def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    print("\n--- Shopping Cart ---")
    total_value = 0
    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        total_value += item_total
        print(f"{item} - R{details['price']:.2f} x {details['quantity']} = R{item_total:.2f}")
    print(f"\nTotal Cart Value: R{total_value:.2f}")
    print("----------------------\n")


def main():
    cart = {}
    while True:
        print("\nMenu:")
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            view_cart(cart)
            print("Proceeding to checkout, Thank you for shopping with Checkers360!")
            break
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please Enter Between 1 and 4.")


if __name__ == "__main__":
    main()
