def unique_code_generator(first_name, last_name):
    number = random.randint(1000000,9999999) #this will give my 4 numbers
    number = str(number) #this converts the number to a string
    fname_slice = first_name[0:3] #this slices fname to 2 characters
    user_name = fname_slice + last_name + number
    return user_name #retunrns a lower case booking code


def ticket_booking(car_list):
    confirmed_booking = []
    total_cost = 25
    ticket_type = int(input("Please input the type of ticket would you like to book to its correspodning number \n \n (1.)  Mitre 10 Mega Stand (Seated) [Cost: $129] \n (2.)  Rear General Admisssion (Standing) [Cost: $185] \n (3.)  North Stand (Seated) [Cost: $230] \n (4.)  Side View (Seated) [Cost: $260] \n (5.)  Front General Admission (Standing) [Cost: $375]"))
    ticket_type = ticket_type*2-2
    ticket_quantity = int(input("How many tickets for {} for?".format(ticket_list[ticket_type])))
    first_name = str(input("Please enter your first name"))
    last_name = str(input("Please enter your last name"))
    cellphone_number = int(input("Please input your cellphone number"))
    ticket_cost = ticket_list[ticket_type + 1] * ticket_quantity #calculates the cost of the booking

    import time #FOR SOME REASON, WHEN I DELETE THESE TWO LINES OF CODE, IF YOU DONT CONFIRM IT REPEATS THE MESSAGE TWICE
    ticket_list #FOR SOME REASON, WHEN I DELETE THESE TWO LINES OF CODE, IF YOU DONT CONFIRM IT REPEATS THE MESSAGE TWICE
    while True:
        choice = int(input("Do you want to confirm your booking? \n \n 1)  YES \n 0)  NO"))
        if choice == 1:
            ticket_booking(ticket_list)
        if choice == 0:
            break

    confirmed_booking.append(ticket_list[ticket_type]) #this adds all of the variables to confirmed booking list
    confirmed_booking.append(ticket_list[ticket_type+1])
    confirmed_booking.append(ticket_cost)
    confirmed_booking.append(first_name)
    confirmed_booking.append(last_name)
    confirmed_booking.append(cellphone_number)

    print("*** Confirmed Booking ***")
    print("Ticket Type: {}".format(confirmed_booking[0]))
    print("Cost of ticket: {} is ${}".format(confirmed_booking[0], confirmed_booking[1]))
    print("Total cost of ticket(s) ${}".format(confirmed_booking[2]))
    print("First name: {}".format(confirmed_booking[3]))
    print("Last name: {}".format(confirmed_booking[4]))
    print("Cellphone number: {}".format(confirmed_booking[5]))
    print("*** End of Confirmed Booking ***")

def main_menu():
    import time
    global ticket_list
    ticket_list = ["Mitre 10 Mega Stand (Seated)", 129, "Rear General Admisssion (Standing)", 185, "North Stand (Seated)", 230, "Side View (Seated)", 260, "Front General Admission (Standing)", 375]
    print("Welcome to Speedy Car Rentals")
    choice = 99
    while choice != 0:
        print("Please select from one of the following options:")
        print("0 to exit")
        print("1 to make a booking")
        choice = int(input("Please enter your choice: \n 1 For a booking \n 0: TO QUIT"))
        if choice == 1:
            ticket_booking(ticket_list)
        if choice == 0:
            break
    print("PROGRAM ENDS")
    quit()

main_menu()