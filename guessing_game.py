"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
import random
from statistics import mean
from statistics import mode
from statistics import median

score_list = []

def add_to_list(count):
    score_list.append(count)

def start_game():
    answer = random.randint(1,100)
    print(answer)
    count = 0    
    print("Welcome to my Guessing Game")
    while True:
        guessed_number = input("Enter a number between 1 and 100:  ")
        try:
            guessed_number = int(guessed_number)
            if guessed_number > 100:
                raise ValueError
            elif guessed_number < 0:
                raise ValueError
        except ValueError:
            print("Please enter a number")
        else:
            count += 1
            if guessed_number > answer:
                print("It's lower, try again")
            elif guessed_number < answer:
                print("It's higher, try again")
            else:
                print(f"Got it! It took you {count} tries! ")
                add_to_list(count)
                repeat = input("Would you like to play again Y/N?  ")

                while True:
                    if repeat == "Y":
                        start_game()
                    else:
                        repeat == "N"
                        print(f"GAME OVER, GOOD BYE \n Mean: {mean(score_list)} \n Median: {median(score_list)} \n Mode: {mode(score_list)}")
                        break
                break
start_game()


    
        