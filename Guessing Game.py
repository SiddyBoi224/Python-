import random
import math

attempt = int(input("Enter the number of attempts: "))
attempt = attempt - 1

lower = int(input("Enter Lower limit: "))
upper = int(input("Enter Upper limit: "))

answer = random.randint(lower,upper)

count = 0


while attempt >= count:
    guess = int(input("Enter input: "))
    if(guess == answer):
        print("Congratulations. You guessed the correct answer.")
        break
    if(attempt == 1):
            print("Last attempt. Try again")
    if(attempt == 0):
            print("You have no attempts left. Thanks for playing loser.")
    else:
        print("Incorrect answer. You have " + str(attempt) + " remaining.")
    attempt = attempt - 1



    

