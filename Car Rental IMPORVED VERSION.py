import random
import datetime

def car_prices(cars_list):
    print("These are the prices for our cars...")
    count = 0
    while count <len(cars_list):
        print(int(count/2+1)," ", cars_list[count], "$", cars_list[count + 1])
        count += 2
    print("*"*20)

def force_number(message, lower, upper):
    while True:
        try:
            number=int(input(message)) #asking for a number
            if number >= lower and number <=upper: #checks the boundaries
                break
            else:
                print("ERROR! Please enter in a number from {} - {}".format(lower,upper))
        except: #if you type in A-Z the following line will run
            print("ERROR! Please enter a number NOT TEXT")
    return number #only a valid number will be returned

def force_name(message, lower, upper):
    while True: #infinite Loop that will keep repeating until the if statement is met
        name=str(input(message)).title() #personalised input message which is passed as a parameter
        if len(name)>=lower and len(name)<=upper and name.isalpha(): #ensures name is 2-20 characters and A-Z
            break
        else:
            print("ERROR.{}, please enter text only".format(message))
        return name #this returns a valid name that is 2-20 characters and A-Z

def code_generator(first_name, last_name):
    a = first_name[0:2] #slices 2 characters
    b = last_name
    random_number = random.randint(100000, 999999) #generate a 6 digit number
    random_number = str(random_number)
    user_name = random_number+a+b #combines the random number/string
    return user_name.upper()

def car_booking(car_list):
    confirmed_booking = []
    car_number = int(input("Which number car would you like to book? (1-9) ",1,9))
    car_number = car_number*2-2
    car_days = int(input("How many days would you like the {} for?".format(cars_list[car_number]),1,30))
    #this ensures that the user can only type a valid name A-Z ,2-30 characters
    first_name = force_name("Please enter your first name",2,10)
    last_name = force_name("Please enter your last name",2,20)

    unique_code = code_generator(first_name, last_name) #this will generate a 6 digit random number
    car_cost = car_list[car_number + 1] * car_days
    #this will add all of the above variables to the confirmed booking list
    confirmed_booking.append("Vehicles: {}".format(cars_list[car_number])) #this adds all of the variables to confirmed booking list
    confirmed_booking.append("${}".format(cars_list[car_number+1]))
    confirmed_booking.append("Daily car price {}".format(car_cost))
    confirmed_booking.append("First name:{}".format(first_name))
    confirmed_booking.append("Last name:{}".format(last_name))
    confirmed_booking.append("Your unique code: {}".format(unique_code))

    #this prints out every item in the booking list
    print("*** Confirmed Booking ***")
    print("Car model: {}".format(confirmed_booking[0]))
    print("The daily hire cost of the {} is ${}".format(confirmed_booking[0], confirmed_booking[1]))
    print("The total hire cost will be ${}".format(confirmed_booking[2]))
    print("First name: {}".format(confirmed_booking[3]))
    print("Last name: {}".format(confirmed_booking[4]))
    print("booking code: {}".format(confirmed_booking[5]))
    #this prints out every item in the booking list
    print("*** End of Confirmed Booking ***")
    for item in confirmed_booking:
        print(item)
    print("*** End of confirmed booking ***")

def main_menu():
    cars_list = ["Fiesta", 100, "Focus", 130, "Mondeo", 160, "Falcon", 230, "Territory", 280, "XR6 Ute", 250, "F150 Truck", 300, "Mustang", 350]
    print("Welcome to Speedy Car Rentals")
    while True:
        print("Please select from one of the following options:")
        print("0 to exit")
        print("1 for the price list")
        print("2 to make a booking")
        choice = int("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 TO QUIT")
        if choice == 1:
            car_prices(cars_list)
        if choice == 2:
            car_booking(cars_list)
        if choice == 0:
            break
    print("PROGRAM ENDS")
    quit()

main_menu()