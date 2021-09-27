import random
from datetime import date

def unique_code_generator(first_name, last_name):
    number = random.randint(1000000,99999999)
    number = str(number) #this converts the number to a string
    fname_slice = first_name[0:2] #this slices fname to 2 characters
    user_name = number + fname_slice.upper() + last_name.upper()
    return user_name


def ticket_booking(car_list):
    confirmed_booking = []
    total_cost = 0
    ticket_type = int(input("Please input the type of ticket would you like to book to its correspodning number \n \n (1.)  Mitre 10 Mega Stand (Seated) [Cost: $129] \n (2.)  Rear General Admisssion (Standing) [Cost: $185] \n (3.)  North Stand (Seated) [Cost: $230] \n (4.)  Side View (Seated) [Cost: $260] \n (5.)  Front General Admission (Standing) [Cost: $375]"))
    ticket_type = ticket_type*2-2
    ticket_quantity = int(input("How many tickets for {} for?".format(ticket_list[ticket_type])))
    first_name = str(input("Please enter your first name"))
    last_name = str(input("Please enter your last name"))
    cellphone_number = int(input("Please input your cellphone number"))
    ticket_cost = ticket_list[ticket_type + 1] * ticket_quantity #calculates the cost of the booking
    ticket_cost += 25
    code = unique_code_generator(first_name, last_name)
    concert = ("Rod Stewart - April 2022 - Forsyth Barr")

    while True:
        choice = int(input("Do you want to confirm your booking? \n \n 1)  YES \n 0)  NO"))
        if choice == 1:
            break
        if choice == 0:
            break
        quit()

    confirmed_booking.append(ticket_list[ticket_type]) #this adds all of the variables to confirmed booking list
    confirmed_booking.append(ticket_list[ticket_type+1])
    confirmed_booking.append(concert)
    confirmed_booking.append(ticket_cost)
    confirmed_booking.append(first_name)
    confirmed_booking.append(last_name)
    confirmed_booking.append(cellphone_number)
    confirmed_booking.append(code)



    print("*** Confirmed Booking ***")
    print("Ticket Type: {}".format(confirmed_booking[0]))
    print("Concert: {}".format(concert))
    print("Cost of ticket: {} is ${}".format(confirmed_booking[0], confirmed_booking[1]))
    print("Total cost of ticket(s) ${}".format(confirmed_booking[3]))
    print("First name: {}".format(confirmed_booking[4]))
    print("Last name: {}".format(confirmed_booking[5]))
    print("Cellphone number: {}".format(confirmed_booking[6]))
    print("Unique ID: {}".format(confirmed_booking[7]))
    print("*** End of Confirmed Booking ***")

    outF = open("orders.txt", "a") #open the text file
    outF.write("******* TICKETEK CONCERT TICKETS *********** \n")
    for item in confirmed_booking:    #prints each item on the pizza order list
        outF.write("{}\n".format(item)) #writes the order of the pizza
        print(confirmed_booking)
    print("********* Order complete ***********")
    today = date.today()
    outF.write("********* Order complete:{} ***********".format(today))
    outF.close()

def main_menu():
    import time
    global ticket_list
    ticket_list = ["Mitre 10 Mega Stand (Seated)", 129, "Rear General Admisssion (Standing)", 185, "North Stand (Seated)", 230, "Side View (Seated)", 260, "Front General Admission (Standing)", 375]
    choice = 99
    choice = force_number("Please enter your choice: \n \n (1.)  New booking \n (0.)  QUIT",0,1)
    if choice == 1:
        ticket_booking(ticket_list)
    if choice == 0:
       print("PROGRAM ENDS")
       quit()

main_menu()
