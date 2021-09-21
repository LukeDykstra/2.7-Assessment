import random

#this function checks the users name and ensures that it is a valid name
def force_name(message,lower,upper):
    while True:
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            break
        else:
            print("ERROR,{} No numbers please".format(message))
    return name

def force_year(message, lower, upper):
    while True:
        try:
            year= int(input(message))
            if year>=lower and year<=upper:
                break
            else:
             print("ERROR! {}, please enter a number between {} - {}".format(lower, upper))
        except:
            print("ERROR, please enter a number not text")
    return year

def user_name_generator():
    first_name=force_name("Please enter your first name",2,15)
    last_name=force_name("{}, Plaese enter your last name".format(first_name),2,20)
    last_name_slice=last_name[0]
    date_enrol=force_year("What year did you enrol",2015,2050)
    date_enrol=str(date_enrol)
    date_enrol = date_enrol[2:4]
    random_number=str(random.randint(100,900))
    obhs_username=first_name+last_name_slice+"."+date_enrol+random_number
    obhs_username = obhs_username.lower()
    print("Your user name is: {}".format(obhs_username))


#main program
user_name_generator()