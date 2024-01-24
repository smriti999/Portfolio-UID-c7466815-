def pizza_price_calculator():
    # BPP pizza price calculator
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Initializing pizza price
    PIZZA_PRICE = 12  # Assuming it's a numerical value
    DELIVERY_COST = 2.50  # in euro
    APP_DISCOUNT = 0.25  # (25%) Representing the discount as a decimal

    # Input validation for the number of pizzas
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas <= 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a positive integer!")

    # Input validation for delivery option
    while True:
        delivery_option = input("Is delivery required? (y/n, Y/N, Yes/No) ")
        if delivery_option.lower() in ['y', 'n', 'yes', 'no']:
            break
        else:
            print('Please answer "y" or "n".')

    # Input validation for Tuesday check
    while True:
        is_tuesday = input("Is it Tuesday? (y/n, Y/N, Yes/No) ")
        if is_tuesday.lower() in ['y', 'n', 'yes', 'no']:
            break
        else:
            print('Please answer "(y/n, Y/N, Yes/No)".')

    # Input validation for app usage
    while True:
        app_used = input("Did the customer use the app? (y/n, Y/N, Yes/No) ")
        if app_used.lower() in ['y', 'n', 'yes', 'no']:
            break
        else:
            print('Please answer "y" or "n".')

    # Calculate total pizza cost
    total_pizza_cost = num_pizzas * PIZZA_PRICE

    # Apply delivery cost
    if delivery_option.lower() == 'y':
        if num_pizzas >= 5:
            print("Delivery is free for orders with five or more pizzas.")
        else:
            total_pizza_cost += DELIVERY_COST

    # Apply Tuesday discount
    if is_tuesday.lower() == 'y':
        total_pizza_cost *= 0.5  # 50% discount on Tuesdays
        tuesday=total_pizza_cost
    # Apply app discount
    if app_used.lower() == 'y':
        app_discount_amount = total_pizza_cost * APP_DISCOUNT
        total_pizza_cost -= app_discount_amount

    # Display the total price
    print(f"\nTotal Price: £{total_pizza_cost:.2f}")

    # Generate receipt for billing system
    print("\nReceipt:")
    print("==========================")
    print(f"Pizza Price per Unit:", f"£{PIZZA_PRICE:.2f}".rjust(10))
    print(f"Number of Pizzas: ", f"{num_pizzas}".rjust(8))

    if delivery_option.lower() == 'y' and num_pizzas < 5:
        print(f"Delivery Cost:", f"£{DELIVERY_COST:.2f}".rjust(18))

    if is_tuesday.lower() == 'y':
        print("Tue. Discount Applied:", f"£{tuesday}".rjust(8))

    if app_used.lower() == 'y':
        print(f"App Discount Applied:", f"£{app_discount_amount:.2f}".rjust(9),)

    print("\n---------------------------------")
    print(f"Total Cost:", f"£{total_pizza_cost:.2f}".rjust(20))
    print("===================================")

# Call the function to run the program
pizza_price_calculator()
