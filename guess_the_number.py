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
        if guess < 0 or guess > 20 or guess == 'None' :
            print("Please enter a number greater than 1 and less than 20." )
            guessing_game() 
        elif guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("your guess is too high" )
        elif guess == secret_number:
            print("Good Job, " + name + "! you guessed my number in " + str(guesses_taken) + " guesses!")
            break
        else:
            print("Nope. The number I was thinking of was " + str(secret_number))
            break

guessing_game()

    # Ask player if they want to play again

def play_again():
    play=str(input("\nDo you want to play again (type yes or no): " ))
    if play.lower() == 'yes':
        guessing_game()
    if play.lower() == 'no':
        print("good bye, " + name + "! Hope you had fun")  
        sys.exit(0)
    else:
        print("Not a valid response!" )
        play_again()

play_again()
