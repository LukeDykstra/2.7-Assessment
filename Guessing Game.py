import random

def force_number(message, lower, upper):
    while True:
        try:
            number=int(input(message))
            if number >= lower  and number <=upper:
                break
            else:
                print("ERROR, {}".format(message))
        except:
                print("ERROR, please enter a number e.g 16, NOT TEXT".format(lower, upper))
        return number

def force_name():
    while True: #this is an infont loop checking the validanty of the users name
        first_name = str(input("First name:")).title()
        if len(first_name)>=2 and len(first_name)<=30 and first_name.isalpha():
            break
        else:
            print("ERROR, please enter a first name 2-30 letters")
    return first_name

def guessing_game():
    name = force_name()
    answer = random.randint(1,10)
    guess = int(0)
    count = 0
    while guess != answer:
        guess = force_number("Please enter a number between 1-10",1,10)
        if guess > answer:
            print("Your guess is too high")
        if guess < answer:
            print("Your guess is too low")
        count += 1
    print("You got it right, the answer was {}".format(number))
    print("It took you {} guesses".format(count))

#main programe
guessing_game()