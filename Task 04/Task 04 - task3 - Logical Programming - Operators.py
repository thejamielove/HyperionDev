# below code welcomes the user and asks them to enter their finishing time, in whole minutes, for each event & stored as an integer
# swimming, cycling & running = inputs are stored in these corresponding variables

print("Welcome and congratulations for competing in the Triathlon!\nPlease enter your finishing time, in whole minutes, for the below events: ")
swimming = int(input("Swimming\n >"))
cycling = int(input("Cycling\n >"))
running = int(input("Running\n >"))

# below code calculates the total time the user inputted for each event & prints it out to the user
triathlon_time = swimming + cycling + running
print(f"Total time for triathlon event = {triathlon_time}")

# below block of code, will check if the total "triathlon_time" variable meets the below criteria and will print out the corresponding statement
# Note: qualifying time for awards == to 100 min
if triathlon_time <= 100:
    print("Congratulations! You have been awarded Provincial Colours!") # if time is less than or equal to 100 min

elif (triathlon_time > 100) and (triathlon_time <= 105):
    print("Congratulations! You have been awarded Provincial Half Colours!") # if time is greater than 100 min and less than or equal to 105 min

elif (triathlon_time > 105) and (triathlon_time <= 110):
    print("Congratulations! You have been awarded the Provincial Scroll!") # if time is greater than 105 min and less than or equal to 110 min

elif (triathlon_time > 110) or (triathlon_time < 100):
    print("Unfortunately, you do not meet the qualifying time, no award :(.") # if time is greater than 110 min or less than 100 min of qualifying time