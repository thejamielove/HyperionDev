# While loop used to execute the the below code infinitely (continue)
# This will run until the last condition is met, of the user inputting a valid full name, (break)

while True:
    # Asks user to input their full name
    full_name = input("Please enter your full name:\n >")
    
    # converted full name string into integers using the len function to calculate length of string
    full_name = len(full_name)

# code block of conditions:
    if full_name == 0:
        print("You haven't entered anything. Please enter your full name.")
        continue

    elif full_name <= 4:
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
        continue

    elif full_name >= 25:
        print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
        continue

    else:
        print("Thank you for entering your name.")
        break