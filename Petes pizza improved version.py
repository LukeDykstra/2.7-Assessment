import random
from datetime import date

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

def force_name(message, lower, upper):
    while True: #infinite Loop that will keep repeating until the if statement is met
        name=str(input(message)).title() #personalised input message which is passed as a parameter
        if len(name)>=lower and len(name)<=upper and name.isalpha(): #ensures name is 2-20 characters and A-Z
            break
        else:
            print("ERROR.{}, please enter text only".format(message))
    return name #this returns a valid name that is 2-20 characters and A-Z

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

def unique_code_generator(first_name, last_name):
    number = random.randint(1000,9999) #this will give my 4 numbers
    number = str(number) #this converts the number to a string
    lname_slice = last_name[0:3] #this slices fname to 2 characters
    user_name = lname_slice + first_name + number
    return user_name.lower #retunrns a lower case booking code

def new_order(pizza_list):
    pizza_order=[]   #empty list to hold the entire order
    total_cost = 0
    first_name = force_name("Please enter your first name",2,20)
    last_name = force_name("Please enter your last name",2,30)
    code = unique_code_generator(first_name, last_name) #this calls the unique generator
    pizza_order.append("First name: {}".format(first_name))
    pizza_order.append("Last name: {}".format(last_name))
    pizza_order.append("Booking cide: {}".format(code))
    """pizza_order.append("Unique code {}". format(unique_code))   """
    pick_up = force_number("Type 1 for pickup or 2 delivery",1,2)
    if pick_up==1:
        pizza_order.append("Pickup")
    if pick_up==2:
        cell_number = get_phone_number("Please enter your cellphone",9,12)
        street_number = str(input("Please enter in your street number"))
        street_name = force_name("Please enter in your street name",2,30)
        suburb = force_name("Please enter in your street suburb",2,15)
        total_cost +=8    #adding on the delivery fee
        pizza_order.append("Cellphone: {}".format(cell_number))
        pizza_order.append("Street number: {}".format(street_number))
        pizza_order.append("Street name: {}".format(street_name))
        pizza_order.append("Suburb: {}".format(suburb))
    #asking which pizza they wish to order
    pizza_number = force_number("Which number pizza would you like to book? (1-12)) \n 1: Pepperoni \n 2: Meat",1,12)
    pizza_number = pizza_number*2-2  #this finds the name of the pizza that they want
    quantity= force_number("How many {} pizzas would you like?".format(pizza_list[pizza_number]),1,5)
    total_cost += pizza_list[pizza_number+1]*quantity     #calculates the total cost
    print ("Total cost is ${:.2f}".format(total_cost))       #prints the total price
    pizza_order.append("Pizza: {}".format(pizza_list[pizza_number]))    #adds the pizza name to the order list
    pizza_order.append("Qantity: {}".format(quantity))      #adds the pizza qauntity to the order list
    pizza_order.append("Total cost: ${}".format(total_cost)) #adds the total price to the order list
    print ("******* Pete's Pizzeria ***********")
    outF = open("orders.txt", "a") #open the text file
    outF.write("******* Pete's Pizzeria ***********")
    for item in pizza_order:    #prints each item on the pizza order list
        outF.write("{}\n".format(item)) #writes the order of the pizza
        print(item)
    print("********* Order complete ***********")
    today = date.today()
    outF.write("********* Order complete:{} ***********".format(today))
    outF.close()

def pizza_prices(pizza_list):
    print("These are the prices for our cars....")
    count = 0
    while count <len(pizza_list):
        print(int(count/2+1), " ", pizza_list[count], "${:.2f}".format(pizza_list[count + 1]))
        count += 2
    print("*"*20)

def main_menu():
    pizza_list = ["Pepperoni",8.50, "Meat",8.50, "Margherita",8.50, "BBQ chicken",8.50, "Hawaiian",8.50, "Buffalo",8.50, "Cheese",8.50, "Veggie",13.50, "Supreme",13.50, "The works",13.50, "BBQ sausage",13.50, "Beef & onion",13.50,]
    print("Welcome to Pete's Pizzeria")
    while True:
        choice = force_number("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 TO QUIT",0,2)
        if choice == 1:
            pizza_prices(pizza_list)
        if choice ==2:
            new_order(pizza_list)
        if choice == 0:
            break
    print("********PROGRAM ENDS*********")
    quit() #This will close pyscripter down

main_menu()

