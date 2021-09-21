while True:#infont loop the keeps on repeating untill an age between 1 and 120\\
    try:
        user_age = int(input("pleace enter you age "))
        if user_age>0 and user_age<120:
            break
        else:
            print("ERROR, use age needs to be age between 1 and 120")
    except:
        print("ERROR, please enter in a nuber e.g 16")
print("the age yout entered was {}".format(user_age))