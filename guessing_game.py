from mimetypes import guess_all_extensions
import random

user_name = input("Hello, what's your name?\n")
print(user_name, " I'm thinking of a number between 1-100, try to guess what it is.")
#guess = int(input("guess:"))
num = random.randint(1,100)

run = True
guesses = 0

while run == True :
    guess = (int(input("guess:")))
    if guess == num:
        print("correct! you got it in", guesses)
        run = False
    elif guess < num:
        guesses = guesses + 1
        print("too low, try again")
        
    else:
        guesses = guesses + 1
        print("too high, try again")
        

