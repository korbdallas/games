# This is a game where you get 6 chances to guess the secret number

#!/usr/bin/env python

import random
import sys

print("Hello what is your name? ")
name=input()

secret_number=random.randint(1, 20)

def guessing_game():
    print("Well, " + name + ", I am thinking of a number between 1 and 20")

    # Ask player to guess in 6 tries
    for guesses_taken in range(1, 7):
        print("\nTake a guess")
        guess=int(input())
        if guess < 0 or guess > 20 or guess == '':
            print("Please enter a number greater than 1 and less than 20." )
            guessing_game 
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("your guess is too high" )
        else:
            break

    if guess == secret_number:
        print("Good Job, " + name + "! you guessed my number in " + str(guesses_taken) + " guesses!")
    else:
        print("Nope. The number I was thinking of was " + str(secret_number))

guessing_game()

play_again = str(input("\nDo you want to play again (type yes or no): " ))
if play_again.lower() == 'yes':
    guessing_game()
if play_again.lower() == 'no':
    print("good bye, " + name + "! Hope you had fun")  
    sys.exit(0)
if play_again.lower() != 'yes' or play_again.islower() != "no":
    print("Not a valid response. Good bye, " + name + "!" )
    sys.exit(0)
