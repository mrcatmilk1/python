'''
Higher or Lower Game


- At the begining of the game, the program picks a random number between 1 and 100
- The number is not displayed to the user
- The user repeatedly tries to correctly guess the number.
- Every time the programs tells the user if the correct answer is higher or lower than their guess.
- If the guess is correct, the game stops with a success message


loops: while
basic if/elif/else
import random
random.randint(1, 100)
'''

import random
from termcolor import colored

command = input("Enter to continue, Q + Enter to quit: ")
while command == "":
    answer = random.randint(1, 100)
    guess = int(input("Guess:"))
    while command != "q" and command != "":
        if command != "q" and command != "":
            print(colored("Please enter a valid input.", "red"))
            command = input("Enter to continue, Q + Enter to quit: ")
    while guess != answer:
        if int(guess) > int(answer):
            print(colored("Lower!", "yellow"))
        elif int(guess) < int(answer):
            print(colored("Higher!", "yellow"))
        guess = int(input("Guess:"))
    print(colored("Correct!", "green"))
    command = input("Enter to continue, Q + Enter to quit: ")
    while command != "q" and command != "":
        if command != "q" and command != "":
            print(colored("Please enter a valid input.", "red"))
            command = input("Enter to continue, Q + Enter to quit: ")