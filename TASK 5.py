import random
first_name=str(input("First name?"))
last_name=str(input("Last name?"))
last_name_slice = last_name[0]
date_enrol = int(input("What year did you enrol"))
date_enrol = str(date_enrol)
date_enrol = str(date_enrol[2:4])
random_number = str(random.randint(100,999))
obhs_username = first_name + last_name_slice + "." + date_enrol + random_number
obhs_username = obhs_username.lower()
print("Your username is: {}".format(obhs_username))


