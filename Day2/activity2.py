#!/usr/bin/env python3

# the above line ensures that linux/unix machines understand which version of python to use

# asign all variables that are needed (shorthand)
breakfast, lunch, dinner = "Omelette", "Sandwhiches and a Chocolate Bar", "Fish and Chips"

# print a formatted string containing the above variables in these places(within the string {here.example()})
print(
    f'Today I have eaten {breakfast} for Breakfast, {lunch} for Lunch and {dinner} for my Dinner'
)

# reassign the variables after being called by the print() Function/Method
breakfast = "Fried Egg"
lunch = "5 Almonds"
dinner = "Fish and Chips AGAIN"

# alternative print() statement for updated variables
print(
    f'Tomorrow I will eat {breakfast} for Breakfast, {lunch} for Lunch and {dinner} for my Dinner'
)
