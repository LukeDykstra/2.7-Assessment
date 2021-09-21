import random
import time

def new_order(pizza_list):
    pizza_order=[]   #empty list to hold the entire order
    total_cost = 0
    first_name=str(input("Please enter your first name"))
    last_name=str(input("Please enter your last name"))
    """unique_code = code_generator(first_name,last_name) #CALLS UP UNIQUE CODE"""
    pizza_order.append("First name: {}".format(first_name))
    pizza_order.append("Last name: {}".format(last_name))
    """pizza_order.append("Unique code {}". format(unique_code))   """
    pick_up=int(input("Type 1 for delivery or 2 for pick up"))
    if pick_up==1:
        pizza_order.append("Pickup")
    if pick_up==2:
        cell_number=str(input("Please enter your cellphone"))
        street_number = str(input("Please enter in your street number"))
        street_name = str(input("Please enter in your street number"))
        suburb = str(input("Please enter in your street suburb"))
        total_cost +=8    #adding on the delivery fee
        pizza_order.append("Cellphone: {}".format(cell_number))
        pizza_order.append("Street number: {}".format(street_number))
        pizza_order.append("Street name: {}".format(street_name))
        pizza_order.append("Suburb: {}".format(suburb))
    #asking which pizza they wish to order
    pizza_number = int(input("Which number pizza would you like to book? (1-12)"))
    pizza_number = pizza_number*2-2  #this finds the name of the pizza that they want
    quantity= int(input("How many {} would you like?".format(pizza_list[pizza_number])))
    total_cost += pizza_list[pizza_number+1]*quantity     #calculates the total cost
    print ("Total cost is ${:.2f}".format(total_cost))       #prints the total price
    pizza_order.append("Pizza: {}".format(pizza_list[pizza_number]))    #adds the pizza name to the order list
    pizza_order.append("Qantity: {}".format(quantity))      #adds the pizza qauntity to the order list
    pizza_order.append("Total cost: ${}".format(total_cost)) #adds the total price to the order list
    print ("******* Pete's Pizzeria ***********")
    for item in pizza_order:    #prints each item on the pizza order list
        print(item)
    print("********* Order complete ***********")


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
        choice = int(input("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 TO QUIT"))
        if choice == 1:
            pizza_prices(pizza_list)
        if choice ==2:
            new_order(pizza_list)
        if choice == 0:
            break
    print("********PROGRAM ENDS*********")
    quit() #This will close pyscripter down



main_menu()

