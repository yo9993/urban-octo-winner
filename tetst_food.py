# Define a function to take in the list of items selected by the customer and calculate the total cost
def calculate_total(items_selected):
    # Define a dictionary of menu items and their prices
    menu = {'burger': 5.99, 'fries': 2.99, 'drink': 1.99}
    total_cost = 0
    # Loop through the items selected by the customer
    for item in items_selected:
        # Add the price of each item to the total cost
        total_cost += menu[item]
    # Return the total cost rounded to two decimal places
    return round(total_cost, 2)

# Define a function to take in the customer's order and print the total cost
def take_order():
    # Define an empty list to store the items selected by the customer
    items_selected = []
    # Loop indefinitely until the customer is done ordering
    while True:
        # Prompt the customer for their order and store it in a variable
        order = input("Enter your order (burger/fries/drink) or type 'done' to finish: ")
        # If the customer is done ordering, break out of the loop
        if order == 'done':
            break
        # If the customer enters an invalid order, prompt them to order again
        elif order not in ['burger', 'fries', 'drink']:
            print("Invalid order. Please enter 'burger', 'fries', 'drink', or 'done'.")
        # Otherwise, add the order to the list of items selected by the customer
        else:
            items_selected.append(order)
    # Calculate the total cost using the calculate_total function and print it
    total_cost = calculate_total(items_selected)
    print("Your total is: $" + str(total_cost))

# Call the take_order function to start taking orders
take_order()