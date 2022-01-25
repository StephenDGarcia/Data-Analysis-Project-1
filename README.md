"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
import random
def start_game():
    answer = random.randint(1,100)
    count = 1    
    print("Welcome to my Guessing Game")
    guessed_number = input("Enter a number between 1 and 100:  ")
    try:
        guessed_number = int(guessed_number)
    except ValueError:
        print("Please enter a number")
    else: 
        while guessed_number != answer:
            if guessed_number > answer:
                print("It's lower, try again")
                guessed_number = int(input("Enter a number:  "))
            else:
                print("It's higher, try again")
                guessed_number = int(input("Enter a number:  "))
            count += 1
        print("Got it! It took you {} tries! \n GAME OVER".format(count))

start_game()

input("Would you like to play again Y/N?  ")

while True:
    repeat = input("> ")
    if repeat == "N":
        break
    elif repeat == "Y":
        start_game()
        