# The below code, is a print function that welcomes the User to the restaurant
print("Welcome to Luigi's!" + " Order below!")

# The below code, is an input command, asking the user to input their 3 most favourite food items from the menu
# The variables stored (item1, item2, and item3) are of the 3 items entered by the user
# These items are then processed through the split() method, which splits this string (3 items) into a list based on a specific delimiter.
# In this instance, the delimiter specified in the instructions is a comma: ","
# These 3 items are then stored in the 3 separate variables: item1, item2, item3
# Note: the reason for specifying the comma as a delimiter, is so the split method will store these properly in their respective variables
# Note: The user is prompted to use the comma "," when inputing their 3 items
item1, item2, item3 = input("Please enter your 3 favourite food items from our menu, separating them with ',': ").split(",")

# The below print functions will print out and diplay to the user:
# the string of order confirmation and each ordered item on a separate line:
print("Order confirmation! You have ordered: ")
print(item1)
print(item2)
print(item3)

# Alternative & best practice way to print order:
print(f"\nOrder confirmation! You have ordered:\n{item1}\n{item2}\n{item3}")