# you’re going shopping with your mom. 
# Using input and if and math, enter the price of three
# items and see if it’s below the budget you set. 
# If it is, print out that you can get the stuff. 
# If it isn’t, print that they failed and have to try again.

price1 = int(input("Enter the price of item 1: "))
price2 = int(input("Enter the price of item 2: "))
price3 = int(input("Enter the price of item 3: "))

item_total = price1 + price2 + price3

budget = int(input("Your budget: "))

if item_total <= budget:
    print("Item total does not exceed budget. You can get all your items!")
else: 
    print("Item total exceeded budget. Please try again.")