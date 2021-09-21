def check_name(message):
     while True: #this is an infont loop checking the validanty of the users name
         first_name = str(input("First name:")).title()
         if len(first_name)>=2 and len(first_name)<=30 and first_name.isalpha():
             break
         else:
             print("ERROR, please enter a first name 2-30 letters")
             return first_name





def guessing_game():
    import random
    contestant = check_name("What is your name?")
answer = random.randint(1,10)
guess = int(0)
count = 0
while guess != answer:
    guess = int(input("Guess a number between 1 and 10"))
    if guess > answer: print("Your guess is too high")
    if guess < answer: print("your guess is too low")
    count = count + 1
print ("Well done", contestant, "you got it right, the answer was", answer, "It took you", count,"guesses")

guessing_game()

