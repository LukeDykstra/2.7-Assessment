#-------------------------------------------------------------------------------
import datetime
today=datetime.datetime.now()

def force_name(message, lower, upper):
    while True: #infinite Loop that will keep repeating until the if statement is met
        name=str(input(message)).title() #personalised input message which is passed as a parameter
        if len(name)>=lower and len(name)<=upper and name.isalpha(): #ensures name is 2-20 characters and A-Z
            break
        else:
            print("ERROR.{}, please enter text only".format(message))
        return name #this returns a valid name that is 2-20 characters and A-Z

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

def print_lists(list, item):
    print("we have the following {}".format(item))
    count = 0
    while count < len(list):
        print(count, " ", list[count])
        count += 1
    choice = item_check(list) #this calls the item check function to ensure a valid number is entered
    choice = list[choice]
    return choice

def item_check(item_list):
    while True:
        try:
            item_amount = len(item_list)
            item_type = int(input("Please enter your selected item type 0 - {}".format(item_amount - 1)))
            if item_type >= 0 and item_type < len(item_list):
                break
            else:
                print("ERROR! Please enter a number from 0 to",len(item_list - 1))
        except:
                print("ERROR! Please enter in a number not text")
    return item_type

def salads():
    saladlist = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    saladcount = 0
    print("We have the following salads, you can have as many as you want")
    while saladcount <5:
        print(saladcount, " ", saladlist[saladcount])
        saladcount += 1
    salad_selected_list = []
    while True:
        print("What salads do you want, enter a number")
        saladtype = item_check(saladlist)
        saladwanted = salad_selected_list.append(saladlist[saladtype])
        quit = str(input("You have selected: {} Type Y if thats all you want".format(salad_selected_list)))
        if quit == "y":
            break

def output_order():
    breadorder=[] #empty list
    #this adds the persons entire order details to the list
    breadorder.append(first_name)
    breadorder.append(cellphone)
    breadorder.append(bread_selected)
    breadorder.append(meat_selected)
    breadorder.append(cheese_selected)
    breadorder.append(salad_selected)
    breadorder.append(dressingss_selected)
    breadorder.append(today)
    outputFile = open("sams_orders.txt", "a") #opens the text file
    print("**** Order for {} - {} ****".format(first_name,cellphone)) #test print to pyscripter
    outputFile.write("**** Order for {} - {} ****".format(first_name,cellphone))
    for order in breadorder:
        print (order) #test print to pyscripter
        outputFile.write("{}\n".format(order))
        outputFile.write("**** End of Order: {}.****".format(today))
    print("**** End of Order: {} ****".format(today)) #test print to pyscripter
    outputFile.close() #closes the text file

#This is temporary code to test that the bread subroutine is working
first_name =  force_name("Please enter in your name",2,10)
cellphone = get_phone_number("Please enter in your cellphone")

dressingslist=["BBQ Sauce", "Ranch Dressing", "Mayo", "No Sauce"]
cheeselist=["Swiss", "Feta", "Brie", "Tasty"]
meatlist=["Chicken", "Turkey", "Tuna", "Bacon"]
breadlist = ["White,", "Brown", "Italian", "Granary"]

bread_selected = print_lists(breadlist, "breads")
meat_selected = print_lists(meatlist, "meats")
cheese_selected = print_lists(cheeselist, "cheese")
salad_selected=salads()
dressingss_selected = print_lists(dressingslist, "dressingss")
output_order()