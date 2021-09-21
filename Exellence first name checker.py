while True: #this is an infont loop checking the validanty of the users name
    first_name = str(input("First name:")).title()
    if len(first_name)>=2 and len(first_name)<=30 and first_name.isalpha():
        break
    else:
        print("ERROR, please enter a first name 2-30 letters")

print("The Name You Enterd was \n {}".format(first_name))