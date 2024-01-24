BPP Pizza Price Calculator 

Description
This Python script is a simple pizza price calculator for BPP (Best Pizza Place) that takes user input for the number of pizzas ordered, delivery option,
whether it's Tuesday, and whether the customer used the app. The script calculates the total pizza cost considering pizza price, delivery cost, Tuesday 
discount, and app discount. It then generates a receipt for the billing system.

Features
Input Validation: The script ensures valid input for the number of pizzas, delivery option, Tuesday check, and app usage.
Cost Calculation: Calculates the total pizza cost based on the number of pizzas, delivery option, Tuesday discount, and app discount.
Discounts: Applies discounts for Tuesday and app usage.
Receipt Generation: Generates a detailed receipt for the billing system.

How to Use
Run the Script:
-Execute the script in a Python environment (Python 3.x recommended).
-The user will be prompted to enter information about the order.

Input Information:
-Provide the number of pizzas ordered.
-Answer whether delivery is required.
-Confirm if it's Tuesday.
-Indicate whether the customer used the app.

View Results:
-The script will display the total price and a detailed receipt.

Input Validation
-For the number of pizzas, the script ensures a positive integer is entered.
-For delivery option, Tuesday check, and app usage, the script validates input for 'y', 'n', 'yes', or 'no'.

Discounts
Delivery Discount: 
-Free delivery for orders with five or more pizzas.
-Tuesday Discount: 50% discount on total pizza cost if it's Tuesday.
-App Discount: 25% discount on total pizza cost if the app is used.

Receipt Format
-The receipt includes details such as pizza price per unit, number of pizzas, delivery cost (if applicable), Tuesday discount (if applicable), 
app discount (if applicable), and the total cost.
