from random import choice
from termcolor import colored

words = open("words.txt").read().split()

valid_words = set(words)

solution = choice(words)
attempt = 0
while attempt < 5:
    guess = input("Enter a word: ").upper()

    if len(guess) != 5:
        print(colored("Invalid length", "red"))
        continue

    if not guess.isalpha():
        print(colored("Only A...Z or a..z characters are allowed.", "red"))
        continue

    if guess not in valid_words:
        print(colored("Not a valid word.", "red"))
        continue

    if guess == solution:
        print(colored(guess, "green"))
        break

    attempt += 1

    letters = {}
    for l in solution:
        if l not in letters:
            letters[l] = 1
        else:
            letters[l] += 1

    correct = set()

    misplaced = set()

    for i in range(5):
        if guess[i] == solution[i]:
            correct.add(i)
            if letters[guess[i]] == 1:
                letters.pop(guess[i])
            else:
                letters[guess[i]] -= 1

    for i in range(5):
        if i in correct:
            continue

        if guess[i] in letters:
            misplaced.add(i)

            if letters[guess[i]] == 1:
                letters.pop(guess[i])
            else:
                letters[guess[i]] -= 1

    for i in range(5):
        if i in correct:
            print(colored(guess[i], "green"), end="")
        elif i in misplaced:
            print(colored(guess[i], "yellow"), end="")
        else:
            print(guess[i], end="")
    print()
else:
    print("Solution was: ", colored(solution, "green"))