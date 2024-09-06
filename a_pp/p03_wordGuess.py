"""
CSE 2110: Procedural Programming
Top-Down Design
Word Guess Game

"""

from random import choice

WRONG_LOSE = 6

# Complete these functions.

def hideLetters(*args):
    return ""


def askPlayer(*args):
    return "A"


# Edit this function to add more choices...

def puzzle():
    "Randomly choose a clue and answer"
    puzzles = [
        ("Sports Team", "TORONTO RAPTORS"),
        ("80's Movie", "RAIDERS OF THE LOST ARK"),
        ("Canadian City", "HALIFAX, NOVA SCOTIA")
    ]
    return choice(puzzles)


# DO NOT EDIT any of the code below.

def play():
    # Initialize the game
    clue, answer = puzzle()
    guesses = ""
    wrong = 0
    display = hideLetters(answer, guesses)

    # Letter guessing loop
    while wrong < WRONG_LOSE and "*" in display:
        letter = askPlayer(clue, display, guesses, wrong)
        guesses += letter
        if letter in answer:
            display = hideLetters(answer, guesses)
        else:
            wrong += 1

    # End the game
    if wrong == WRONG_LOSE:
        print("You lose!")
    else:
        print("You win!")
    print(answer)


# Play the game!
play()
