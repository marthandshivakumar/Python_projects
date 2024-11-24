veg = ['brinjal', 'tomato', 'potato', 'onion']
quantity = [15, 20, 25, 10]
price = [45, 20, 30, 50]
item_profit = [0, 0, 0, 0]
itemized_bills = []
revenue = 0
investment = 1000
users_cart = []

# Start main loop
while True:
    print("\n" + "=" * 50)
    print(f"{'Welcome to the Store':^50}")
    print("=" * 50)
    print("\nChoose an option:")
    print("1. Owner")
    print("2. User")
    print("3. Exit")
    
    user_type = input("\nEnter your choice (owner/user/exit): ").strip().lower()

    if user_type == "owner":
        print("\nOwner Panel Selected")
        
        while True:
            print("\n" + "-" * 50)
            print(f"{'Owner Menu':^50}")
            print("-" * 50)
            print("1. Add Item to Inventory")
            print("2. Remove Item from Inventory")
            print("3. Update Item in Inventory")
            print("4. View Inventory")
            print("5. View Users and Their Carts")
            print("6. View Report")
            print("7. Exit Owner Panel")
            print("-" * 50)
            
            owner_choice = input("\nChoose an option: ").strip()

            if owner_choice == "1":  # Add Item
                item = input("Enter the vegetable name to add: ").strip()
                if item in veg:
                    print(f"{item} already exists in the inventory!")
                    continue
                quantity.append(int(input(f"Enter quantity for {item}: ")))
                price.append(float(input(f"Enter price per kg for {item}: ")))
                veg.append(item)
                item_profit.append(0)
                print(f"{item} added to the inventory!")

            elif owner_choice == "2":  # Remove Item
                print("\nCurrent Inventory:")
                for v, q, p in zip(veg, quantity, price):
                    print(f"{v:<10} - {q:>3}kg at Rs.{p:>3}/kg")
                item = input("Enter the vegetable name to remove: ").strip()
                if item in veg:
                    idx = veg.index(item)
                    veg.pop(idx)
                    quantity.pop(idx)
                    price.pop(idx)
                    item_profit.pop(idx)
                    print(f"{item} removed from the inventory!")
                else:
                    print(f"{item} is not in the inventory!")

            elif owner_choice == "3":  # Update Item
                print("\nCurrent Inventory:")
                for v, q, p in zip(veg, quantity, price):
                    print(f"{v:<10} - {q:>3}kg at Rs.{p:>3}/kg")
                item = input("Enter the vegetable name to update: ").strip()
                if item in veg:
                    idx = veg.index(item)
                    new_quantity = int(input(f"Enter new quantity for {item}: "))
                    new_price = float(input(f"Enter new price for {item}: "))
                    quantity[idx] = new_quantity
                    price[idx] = new_price
                    print(f"{item} updated in the inventory!")
                else:
                    print(f"{item} is not in the inventory!")

            elif owner_choice == "4":  # View Inventory
                print("\nCurrent Inventory:")
                for v, q, p in zip(veg, quantity, price):
                    print(f"{v:<10} - {q:>3}kg at Rs.{p:>3}/kg")

            elif owner_choice == "5":  # View Users and Their Carts
                print("\nUsers and their carts:")
                if users_cart:
                    for user in users_cart:
                        print(f"User: {user['name']} ({user['mobile']})")
                        for item, qty, total in user['cart']:
                            print(f"   {item:<10} - {qty:>3}kg for Rs.{total:>3}")
                else:
                    print("No users found!")

            elif owner_choice == "6":  # View Report
                print("\nStore Report")
                print(f"Total Revenue: Rs.{revenue}")
                print(f"Total Profit: Rs.{sum(item_profit)}")
                for v, p, q, ip in zip(veg, price, quantity, item_profit):
                    print(f"{v:<10} - Price: Rs.{p:>3}/kg, Stock: {q:>3}kg, Profit: Rs.{ip:>3}")

            elif owner_choice == "7":  # Exit Owner Panel
                print("\nExiting Owner Panel...")
                break

            else:
                print("\nInvalid option. Please choose a valid option from the menu.")
                continue

    elif user_type == "user":
        print("\nUser Panel Selected")
        username = input("Enter your name: ").strip()
        mobile = input("Enter your mobile number: ").strip()
        user_cart = []  # Individual user's cart

        while True:
            print("\n" + "-" * 50)
            print(f"{'User Menu':^50}")
            print("-" * 50)
            print("1. Add Item to Cart")
            print("2. Remove Item from Cart")
            print("3. Modify Item Quantity in Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit User Panel")
            print("-" * 50)
            
            user_choice = input("\nChoose an option: ").strip()

            if user_choice == "1":  # Add Item to Cart
                print("\nAvailable Vegetables:")
                for v, q, p in zip(veg, quantity, price):
                    print(f"{v:<10} - {q:>3}kg at Rs.{p:>3}/kg")
                item = input("Enter the vegetable name to add to cart: ").strip()
                if item in veg:
                    idx = veg.index(item)
                    qty = int(input(f"Enter quantity for {item} (Available: {quantity[idx]}kg): "))
                    if qty <= quantity[idx]:
                        total_price = qty * price[idx]
                        user_cart.append([item, qty, total_price])
                        quantity[idx] -= qty
                        print(f"{item} added to your cart!")
                    else:
                        print(f"Not enough stock for {item}!")
                else:
                    print(f"{item} is not available!")

            elif user_choice == "2":  # Remove Item from Cart
                print("\nYour Cart:")
                for item, qty, total in user_cart:
                    print(f"{item:<10} - {qty:>3}kg for Rs.{total:>3}")
                item = input("Enter the vegetable name to remove from cart: ").strip()
                user_cart = [i for i in user_cart if i[0] != item]
                print(f"{item} removed from your cart!")

            elif user_choice == "3":  # Modify Item Quantity in Cart
                print("\nYour Cart:")
                for item, qty, total in user_cart:
                    print(f"{item:<10} - {qty:>3}kg for Rs.{total:>3}")
                item = input("Enter the vegetable name to modify quantity: ").strip()
                for i in range(len(user_cart)):
                    if user_cart[i][0] == item:
                        new_qty = int(input(f"Enter new quantity for {item}: "))
                        user_cart[i][1] = new_qty
                        user_cart[i][2] = new_qty * price[veg.index(item)]
                        print(f"{item} quantity updated in your cart!")
                        break

            elif user_choice == "4":  # View Cart
                print("\nYour Cart:")
                for item, qty, total in user_cart:
                    print(f"{item:<10} - {qty:>3}kg for Rs.{total:>3}")
                print(f"\nTotal Bill: Rs.{sum([total for _, _, total in user_cart])}")

            elif user_choice == "5":  # Checkout
                print("\nCheckout Summary:")
                for item, qty, total in user_cart:
                    print(f"{item:<10} - {qty:>3}kg for Rs.{total:>3}")
                total_bill = sum([total for _, _, total in user_cart])
                print(f"\nTotal Bill: Rs.{total_bill}")
                revenue += total_bill
                users_cart.append({'name': username, 'mobile': mobile, 'cart': user_cart})
                user_cart.clear()
                print(f"\nThank you for your purchase, {username}!")
                break

            elif user_choice == "6":  # Exit User Panel
                print("\nExiting User Panel...")
                break

            else:
                print("\nInvalid option. Please choose a valid option from the menu.")
                continue

    elif user_type == "exit":
        print("\nThank you for visiting the store!")
        break

    else:
        print("\nInvalid input! You have entered something wrong, and the program is exiting.")
        break
