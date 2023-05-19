# Welcomes user to program
print("Hello and Welcome to the Simple Calculator Application!\n")

result = "" # sets up result variable for calculations
filename = "" # sets up filename variable for user to store calculation results in txt file
results_list = [] # stores user calculation inputs, ready to be printed in txt file
operator_check = ["+", "-", "/", "*"] # check list to make sure user enters appropriate operator signs


# block of code starts program & asks the user to input an option (1, 2, 3 or 4)
while True:
    print("\nPlease choose from the below options, by entering 1, 2, 3 or 4:\n")
    print("1. To use the Simple Calculator")
    print("2. To save calculation results to a txt file")
    print("3. To view previous saved calculation results from a txt file")
    print("4. To end the program\n")

    option = input("Option:\n > ").lower()

    # option 4 ends program
    if option == "4":
        print("\nThank you for using the Finance Calculator! Have a good day :).\n")
        break   
    
    # check - if user did not enter the appropriate options left (1, 2 or 3)
    # this will let the user know that they did not enter a viable option and the loop will start back to the beginning
    elif option != "1" and option != "2" and option !="3":
        print("\nYou did not enter a valid option. Please try again.\n")
        continue

    # block of code for option 1 = finance calculator
    elif option == "1":

        try:
            num1 = float(input("Please enter the 1st number:\n > "))
            num2 = float(input("Please enter the 2nd number:\n > "))
        
        # check to make sure user enters in a whole number or decimal number
        except ValueError:
            print("\nYou did not enter a valid calculation. Please try again.\n")
            continue

        operator = input("Please enter an operator ('+', '-', '/', '*'):\n > ").lower()

        # check - if user inputed the appropriate operator based on the operator list
        if operator not in operator_check:
            print("\nYou did not enter a valid operator, please try again.\n")
            continue
        
        # below sets up operator calculations and are stored in the result variable
        if operator == '+':
            result = num1 + num2
        
        elif operator == '-':
            result = num1 - num2
        
        elif operator == '/':
            if num2 == 0:
                print("\nError: Division by 0 is not allowed.\n")
                continue
            result = num1 / num2

        elif operator == '*':
            result = num1 * num2
        
        # below stores & saves the user calculations & results to the results_list variable
        # the append function is used to add to the list of individual calculation the user may perform
        results_list.append((num1, operator, num2, result))
        print(f"\n{num1:,.2f} {operator} {num2:,.2f} = {result:,.2f}\n") # prints calculation results to user in terminal

    # block of code for option 2 = printing & storing calculation results to txt file
    elif option == "2":
        if len(results_list) == 0: # checks to make sure a calculation has been peformed first by checking the results_list variable
            print("\nA calculation has not been performed to be saved. Please perform a calculation first.\n")
            continue

        # user inputs file name
        filename = input("Please enter a name for the text file (without extension):\n > ")

        # check to make sure user doesn't enter a file extension with name
        if "." in filename:
            print("\nError: file name cannot contain '.(file extension)'. Please try again\n")
            continue

        # below writes the stored calculations in the results_list variable to the txt file
        with open(f"{filename}.txt", "w") as file:
            for calculation in results_list:
                num1, operator, num2, result = calculation
                file.write(f"\n{num1:,.2f} {operator} {num2:,.2f} = {result:,.2f}")

        # displays to user the file name saved
        print(f"\nResults saved to {filename}.txt\n")

        # reads the file contents to the user in the terminal
        with open(f"{filename}.txt", "r") as file:
            contents = file.read()
            print(f"File contents:\n {contents}\n")

    # block of code for option 3 = to view previous saved calculation results from a txt file
    elif option == "3":
        # user inputs existing saved file name
        filename = input("Please enter existing file txt file name (without extension):\n > ")

        # check to make sure user doesn't enter a file extension with name
        if "." in filename:
            print("\nError: file name cannot contain '.(file extension)'. Please try again\n")
            continue
                
        # reads the file contents to the user in the terminal
        try:
            with open(f"{filename}.txt", "r") as file:
                contents = file.read()
                print(f"\nFile contents from {filename}.txt:\n {contents}\n")
        
        # Check - to make sure user inputed an exisiting saved txt file
        except Exception as error:
            print(f"Failed to open saved txt file. Please try again. Error: {error}\n")
            continue

