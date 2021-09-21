def check_name(message,lower,upper):
    while True: #this is an infont loop checking the validanty of the users name
        name = str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            break
        else:
            print("ERROR, please enter a  name {} - {} letters".format(message,lower,upper))
    return name


#This is my main program
first_name = check_name("Please enter a first name",2,20)
middle_name = check_name("Please enter a middle name",2,20)
last_name = check_name("Please enter a Last name",2,20)
inishals = check_name("please enter your entatials",2,5).upper()
print("the name you enterd is {} {} {} ({})".format(first_name, middle_name, last_name, inishals))