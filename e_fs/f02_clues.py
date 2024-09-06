"""
CSE 2130: Files & File Structures
Reading Text Files
"""

from random import choice

# Complete this function only...

def readPuzzles(filename="resource/puzzles.txt"):
    return []


# DO NOT EDIT any of the code below.

def main():
    puzzles = readPuzzles()
    clue, answer = choice(puzzles)
    print("{}: {}".format(clue, answer.upper()))

main()
