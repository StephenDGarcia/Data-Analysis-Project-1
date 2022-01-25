"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
import random
def start_game():
    answer = random.randint(1,100)
    print(answer)
    count = 0    
    print("Welcome to my Guessing Game")
    while True:
        guessed_number = input("Enter a number between 1 and 100:  ")
        try:
            guessed_number = int(guessed_number)
        except ValueError:
            print("Please enter a number")
        else:
            count += 1
            if guessed_number > answer:
                print("It's lower, try again")
            elif guessed_number < answer:
                print("It's higher, try again")
            else:
                print("Got it! It took you {} tries! \n GAME OVER".format(count))
                break
start_game()

repeat = input("Would you like to play again Y/N?  ")
while True:
    if repeat == "N":
            break
    elif repeat == "Y":
        start_game()
        