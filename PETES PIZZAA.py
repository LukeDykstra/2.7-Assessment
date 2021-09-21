def new_order(pizza_list):
    pizza_order = []
    total_cost=0
    first_name = str(input("Please enter your first name"))
    last_name = str(input("Please enter your last name"))
    #unique code genrator
    pick_up=int(input("Would you like Pickup 1 or 2 for Delivery"))
    if pick_up==1:
        pizza_order.append(first_name)
        pizza_order.append(last_name)
    if pick_up ==2:
        total_cost+=8
        street_number = int(input("Please enter your street number"))
        street_name = str(input("Please enter your street name"))
        suburb = str(input("Please enter your suburb name"))



    pizza_number = int(input("Which number pizza would you like to order? (1-13) \n 1: Hawaii \n 2: Meat lovers \n 3: The ROBERT DELIGHT \n 4: Chicken Mayo \n 5: Vegeterian Deluxe \n 6: Beef and Onion \n 7: Pepperoni \n 8: New York Style \n 9: Margherita \n 10: Cheese Supreme \n 11: The Rory Special"))
    pizza_number = pizza_number*2-2
    pizza_quantity= int(input("How many {} do you want?" .format(pizza_list[pizza_number])))
    total_cost= pizza_quantity * pizza_list[pizza_number+1]
    print("Price {}".format(total_cost))


    pizza_order.append(pizza_list[pizza_number])
    pizza_order.append(pizza_list[pizza_number+1])

def pizza_prices(pizza_list):
    print("These are the prices for our pizzas...")
    count = 0
    while count <len(pizza_list):
        print(int(count/2+1)," ", pizza_list[count], "$", pizza_list[count + 1])
        count += 2
    print("*"*20)



def main_menu():
    import time

    pizza_list = ["Hawaii", 8.50, "Meat lovers", 8.50, "The Robert Delight", 13.50, "Chicken Mayo", 8.50, "Vegeterian Deluxe", 8.50, "Beef & Onion", 8.50, "Buffalo", 8.50, "Pepperoni", 13.50, "New York Style", 13.50, "Margherita", 13.50, "Cheese Supreme", 13.50, "The Rory Special", 13.50,]
    print("Welcome to Pete's Pizza")
    choice = 99
    while choice != 0:
        choice = int(input("Please enter your choice: \n 1: Prices \n 2: New Order \n 3: Quit"))
        if choice == 1:
            pizza_prices(pizza_list)
        if choice == 2:
            new_order(pizza_list)
        if choice == 3:
            break
    print("PROGRAM ENDS")
    quit()

main_menu()


