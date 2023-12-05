# Assign two different movies, two different ticket costs. 
# Assign the cost of popcorn, candy, drinks, nachos, and a hotdog.
# If one person goes to movie #1 and buys a hotdog, drink, and candy, 
# how much does it cost? Print this number. If person #2 buys nachos and popcorn, 
# how much does it cost them? Print this number too and decide who 
# spends more money at the movies.

movie_1 = 8 
movie_2 = 14

popcorn = 12
candy = 5
drinks = 2
nachos = 10
hotdog = 3

person1_cost = movie_1 + hotdog + drinks + candy
person2_cost = movie_2 + nachos + popcorn

print("Person 1 Cost: ", person1_cost, "dollars")
print("Person 2 Cost: ", person2_cost, "dollars")

print("Person 2 spent more money.")


