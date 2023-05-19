# Welcomes the user to the Average calculator
# numbers_list variable is used to store the 'number' variable inputs into a list, that the user enters into the program, except '-1' stop command
print("Hello and Welcome to the Average Calculator!")
numbers_list = []
number = int(input("Please enter a number to proceed. Note that entering '-1' will stop the program from requesting a number:\n > "))

# While loop will continue to execute, until the user enters '-1' to stop the program
# append function is used to add in the new number variable, a user has entered, to the end of the numbers_list variable. Example [10,5,6,9,...]
while number != -1:
    numbers_list.append(number)
    number = int(input("Please enter another number, or enter '-1' to stop:\n > "))

# once user stops the program '-1', the below will calculate and print:
# sum numbers user has entered in list / count numbers entered using the len function in list = average
average = sum(numbers_list) / len(numbers_list)
print(f"Average calculated, based on your inputs, comes to: {average:.2f}")