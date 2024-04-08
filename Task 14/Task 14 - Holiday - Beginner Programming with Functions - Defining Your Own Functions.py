# block of code to set-up functions for the holiday trip planner program & calculations
def plane_cost(city_flight):
    if city_flight == "barcelona":
        return 300
    
    elif city_flight == "london":
        return 350
    
    elif city_flight == "rome":
        return 250
    
    elif city_flight == "new york":
        return 500

def hotel_cost(num_nights):
    return 150 * num_nights

def car_rental(rental_days):
    return 50 * rental_days

def holiday_cost(plane_cost, hotel_cost, car_rental):
    return plane_cost + hotel_cost + car_rental

def destination_options():
    print("\nPlease choose from the below Flight Destinations:\n")
    print("Barcelona = £300.00")
    print("London = £350.00")
    print("Rome = £250.00")
    print("New York = £500.00")
    print("End = ends program\n")
    print("Note: The flight price is inclusive of roundtrip airfare\n")

# check: to make sure user enters destination options defined in "plane_cost" function
destination_options_check = ["barcelona", "london", "rome", "new york", "end"]

# block of code to run through holiday trip planner using while loop
while True:

    print("\nHello & Welcome to your holiday trip planner!")
    print("Hotel & Car Rental prices will not change for each destination:\n")
    print("Hotel = £150 per night")
    print("Car Rental = £50 per day")
    destination_options() # runs the print out from the "destination_options" function

    city_flight = input("Please enter your Flight Destination from the above options\n > ").lower() #variable declared in "plane_cost" function

    # check: to make sure user enters the available destinations
    if city_flight not in destination_options_check:
        print("\nYou did not enter a valid option, please try again.\n")
        continue

    elif city_flight == "end":
        break

    # check: to make sure user enters a whole number for the Hotel & Car Rental days/nights
    try:
        num_nights = int(input("Please enter the number of nights you will be staying at a hotel\n > ")) #variable declared in "hotel_cost" function
        if num_nights < 0: # check: to make sure that the user enters # of nights greater than or equal to 0 (in case the user does not need a hotel)
            print("\nInvalid option. Number of Nights entered for your hotel stay need to be more than or equal to 0.\n")
            continue
        
        rental_days = int(input("Please enter the number of days you will be hiring a car\n > ")) #variable declared in "car_rental" function
        if rental_days < 0: # check: to make sure that the user enters # of days greater than or equal to 0 (in case the user does not need a car)
            print("\nInvalid option. Number of Days for hiring a car need to be more than or equal to 0.\n")
            continue
    
    except ValueError:
        print("\nYou did not enter a whole number. Please try again.\n")
        continue

    # variables to hold the calculated holiday cost from user inputs & calculations set from functions
    flight_total = plane_cost(city_flight)
    hotel_total = hotel_cost(num_nights)
    car_rental_total = car_rental(rental_days)
    total_cost = holiday_cost(flight_total, hotel_total, car_rental_total)

    # print out of holiday details & breakdown of costs for the trip
    print("\nHoliday Details:\n")
    print(f"Destination Choice: {city_flight.upper()}")
    print(f"Flight Cost: £{flight_total:,.2f}")
    print(f"Hotel Cost: £{hotel_total:,.2f}")
    print(f"Car Rental Cost: £{car_rental_total:,.2f}")
    print(f"Total Holiday Cost: £{total_cost:,.2f}")

    # block of code to ask user if they would like to use the program again or to end it
    continue_program = input("\nWould you like to use the Holiday Trip Planner again? Please enter 'Yes' or 'No'\n > ").lower()

    # check: to make sure user entered "yes" or "no"
    if continue_program != "yes" and continue_program != "no":
        print("\nYou did not enter a viable option. Please try again.\n")
        continue

    elif continue_program == "yes":
        continue

    elif continue_program == "no":
        print("\nThank you & Have a lovely day!")
        break