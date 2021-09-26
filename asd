import random
from datetime import date

def unique_code_generator(first_name, last_name):
    number = random.randint(1000000,99999999)
    number = str(number) #this converts the number to a string
    fname_slice = first_name[0:2] #this slices fname to 2 characters
    user_name = number + fname_slice.upper() + last_name.upper()
    return user_name

def get_phone_number(message): #Runs a message through this program
    while True: #While true Loop to filter bad data
        try:
            phone_number = str(input(message)) #Asks for phone number or 0 to quit. Replace there to get rid of all
            if len(phone_number) >= 9 and len(phone_number) <=12 and phone_number.isnumeric(): #If the length of the phone number is between 9 - 12
                break #Breaks function if specifications are met
            else: #If specs aren't met will run this
                print("Cellphone numbers only contain numbers and are between 9 and 12 digits") #Tells user to enter a valid phone number
        except:
                print("Please enter a valid phone number") #Tells user to enter correct phone number
    return phone_number #Will return value to variable that called the function

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

def ticket_booking(car_list):
    confirmed_booking = []
    total_cost = 0
    ticket_type = force_number("Please enter the number that is corresponding to the type of ticket would you like to book \n \n (1.)  Mitre 10 Mega Stand (Seated) [Cost: $129] \n (2.)  Rear General Admisssion (Standing) [Cost: $185] \n (3.)  North Stand (Seated) [Cost: $230] \n (4.)  Side View (Seated) [Cost: $260] \n (5.)  Front General Admission (Standing) [Cost: $375]",1,5)
    ticket_type = ticket_type*2-2
    ticket_quantity = force_number("How many ticket(s) for {} would you like?".format(ticket_list[ticket_type]),1,12)
    first_name = force_name("Please enter your first name",2,20)
    last_name = force_name("Please enter your last name",2,30)
    cellphone_number = get_phone_number("Please enter your cellphone number")
    ticket_cost = ticket_list[ticket_type + 1] * ticket_quantity #calculates the cost of the booking
    ticket_cost += 25
    code = unique_code_generator(first_name, last_name)
    concert = ("Rod Stewart - April 2022 - Forsyth Barr")
    reminded_message = ("***Please remember to bring photo ID to the Regent Theatre in order to pay for and collect their tickets***")

    while True:
        choice = force_number("You have booked in {} ticket(s) of {}. Would you like to confirm? \n \n  (1.)  YES \n  (0.)  NO".format(ticket_quantity, ticket_list[ticket_type]),0,1)
        if choice == 1:
            print(reminded_message)
            break
        if choice == 0:
            quit()

    confirmed_booking.append("Concert: {}".format(concert))
    confirmed_booking.append("Ticket Type: {}".format(ticket_list[ticket_type])) #this adds all of the variables to confirmed booking list
    confirmed_booking.append("Cost of ticket: ${}".format(ticket_list[ticket_type+1]))
    confirmed_booking.append("Quantity of ticket(s):{}".format(ticket_quantity))
    confirmed_booking.append("Total cost: ${}".format(ticket_cost))
    confirmed_booking.append("First name: {}".format(first_name))
    confirmed_booking.append("Last name: {}".format(last_name))
    confirmed_booking.append("Cellphone number: {}".format(cellphone_number))
    confirmed_booking.append("Unique Code: {}".format(code))

    print("*** Confirmed Booking ***")
    print("Ticket Type: {}".format(confirmed_booking[0]))
    print("Concert: {}".format(concert))
    print("Cost of ticket: {} is ${}".format(confirmed_booking[0], confirmed_booking[1]))
    print("Total cost of ticket(s) ${} + $25 fee".format(confirmed_booking[3]))
    print("First name: {}".format(confirmed_booking[4]))
    print("Last name: {}".format(confirmed_booking[5]))
    print("Cellphone number: {}".format(confirmed_booking[6]))
    print("Unique ID: {}".format(confirmed_booking[7]))
    print("*** End of Confirmed Booking ***")

    outF = open("orders.txt", "a") #open the text file
    outF.write(" \n ******* TICKETEK ORDER *********** \n")
    print()
    for item in confirmed_booking:    #prints each item on the pizza order list
        outF.write("{}\n".format(item)) #writes the order of the pizza
        print(item)
    today = date.today()
    outF.write(" \n Thankyou for booking at TICKETEK, please remember to bring photo ID to the Regent Theatre in order to pay for and collect their tickets \n")
    outF.write(" \n ********* ORDER COMPLETED: {} *********** \n ".format(today))
    outF.close()

def main_menu():
    import time
    global ticket_list
    ticket_list = ["Mitre 10 Mega Stand (Seated)", 129, "Rear General Admisssion (Standing)", 185, "North Stand (Seated)", 230, "Side View (Seated)", 260, "Front General Admission (Standing)", 375]
    choice = 99
    while choice != 0:
        choice = int(input("Please enter your choice: \n \n (1.)  New booking \n (0.)  QUIT"))
        if choice == 1:
            ticket_booking(ticket_list)
        if choice == 0:
            break
    print("PROGRAM ENDS")
    quit()

main_menu()
