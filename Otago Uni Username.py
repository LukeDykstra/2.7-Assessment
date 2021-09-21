import random
def force_name(message,lower,upper):
    while True:
        name=str(input(message))
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            break
        else:
            print("ERROR!, please enter in {}".format(message))
            return name

def random_number(first_name, last_name):
    random_number = random.randint(100,999)
    random_number = str(random_number)
    user_name = last_name[0:3] + first_name[0:2] + random_number
    user_name=user_name.lower()
    return user_name

def generate_username():
    first_name = force_name("First name",2,10)
    last_name= force_name("Last name",2,20)
    uni_username = random_number(first_name, last_name)
    print("Otago Uni Username {}".format(uni_user_name))


#MAIN PROGRAM
generate_username()
