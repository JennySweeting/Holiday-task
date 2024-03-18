# Ask user where they are flying to, how many nights they are staying for
    # and for how many days they would like to rent a car

# Print 4 flight destinations including costs 
print("\033[1mReturn Flights\033[0m\n")
print("Berlin - £240pp\nMunich - £210pp\nRome   - £255pp\nZurich - £197pp\n")

# Ask user where they would like to fly to
city_flight = input("Which city would you like to visit? ")
city_flight = city_flight.capitalize()

# Create a while true loop to prompt print statements linked
    # to the city chosen or user to enter valid input
while True:
    if city_flight == "Berlin":
        print("Wunderbar, Berlin!\n")
        break
    elif city_flight == "Munich":
        print("You're going to Munich, how exciting!\n")
        break
    elif city_flight == "Rome":
        print("You know what they say? When in Rome...\n")
        break
    elif city_flight == "Zurich":
        print("Beautiful Switzerland, great choice!\n")
        break
    elif city_flight != "Berlin" or "Munich" or  "Rome" or "Zurich":
        city_flight = input("Oops, I don't think we fly here. Please select a city from the list :) ")
        city_flight = city_flight.capitalize()
        continue

# Prints in bold
print("\033[1mNo. of nights\033[0m\n")

# Ask user how many nights they would like to stay at the hotel
num_nights = input("Your hotel costs £110pn. How many nights will you be staying? ")

# If the user enters a number, print statement is prompted and loop breaks
# If user does not enter a number, they will be prompted to enter a number
while True:
    if num_nights.isnumeric():
        print(f"Great, {num_nights} nights it is!\n")
        break
    else:
        num_nights = input("Please enter a number: ")

num_nights = int(num_nights)

# Prints in bold
print("\033[1mCar rental\033[0m\n")

# Ask user how many days they would like to hire a car for
rental_days = input("Car rental is £45 a day. How many days would you like to hire a car for? ")

# Use a while True loop to print statement if user input is numeric or
    # prompt user to enter a valid number
while True:
    if rental_days.isnumeric():
        if rental_days != 0:
            print(f"{rental_days} days to explore by car. Please don't forget to read up on the " \
                f"highway code in {city_flight}!\n")
            break
    elif rental_days == 0:
        print("No car this trip!\n")
        break
    else:
        rental_days = input("Please enter a number: ")
        continue

# Prints in bold
print("\033[1mTotal holiday costs\033[0m\n")

# Create 3 functions to calculate the cost of each aspect of the holiday:
    # hotel, flights, car rental

def hotel_cost(num_nights):

    ''' This function takes in the user
    input as a parameter to determine the
    number of nights they are staying at the 
    hotel. It calculates the total cost by 
    multiplying this parameter by the nightly 
    cost of the hotel
    '''

    sum_of_hotel = (110 * num_nights)
    sum_of_hotel = int(sum_of_hotel)
    return sum_of_hotel

total_hotel = hotel_cost


def plane_cost(city_flight):

    '''This function takes the user input 
    as a parameter to determine their flight
    destination. It then returns the cost
    of the corresponding flight
    '''

    if city_flight == 'Berlin':
        flight_cost = 240
    elif city_flight == 'Munich':
        flight_cost = 210
    elif city_flight == 'Rome':
        flight_cost = 255
    elif city_flight == 'Zurich':
        flight_cost = 197
    return flight_cost
    
total_flight = plane_cost


def car_rental(rental_days):

    '''This function calculates the 
    cost of car rental by taking the 
    number of rental days as a parameter
    and multiplying by the daily rental 
    cost
    '''

    rental_days = int(rental_days)
    car_cost = rental_days*45
    return car_cost

total_car_rental = car_rental

# Create function to calculate and print the total costs of the holiday

def holiday_cost(total_hotel, total_flight, total_car_rental):

    '''This function takes the previous functions
     as parameters and adds them together
    to calculate the total cost of the holiday.
    It prints the costs of: flights, hotel, 
    car rental and total holiday cost
    '''

    print("The cost of your hotel is: \t\t£", end='')
    print(total_hotel)
    print("The cost of your return flights is: \t£", end='')
    print(total_flight)
    print("The cost of your hire car is: \t\t£", end='')
    print(total_car_rental)
    total_holiday = total_hotel + total_flight + total_car_rental
    print("The \033[1mtotal\033[0m cost of your holiday is: \t£", end='')
    print(total_holiday)


holiday_cost(total_hotel(num_nights), total_flight(city_flight), total_car_rental(rental_days))