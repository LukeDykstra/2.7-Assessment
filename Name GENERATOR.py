import random

def unique_code_generator(first_name, last_name):
    number = random.randint(100,99999)
    number = str(number) #this converts the number to a string
    fname_slice = first_name[0:2] #this slices fname to 2 characters
    user_name = number + fname_slice.upper() + last_name.upper()
    return user_name

#main program
first_name = str(input("What is your first name"))
last_name = str(input("What is your last name"))
booking_code = unique_code_generator (first_name, last_name)
print(booking_code)
