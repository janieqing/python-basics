# You have $10 to spend shopping. 
# Make variables for the cost of 3 items you want to 
# buy and use an if statement to see if you can afford 
# everything you got. If you can afford it, print a message.
# If you cannot afford it, print that you can’t and 
# print how much money they all cost. 

item1 = 3
item2 = 7
item3 = 1
total = item1 + item2 + item3

money = 10

if money > total:
    print(total)
else:
    print("Unable to afford items.")