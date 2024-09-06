"""
CSE 2110: Procedural Programming
Functions
Example 1

"""

from random import randint

def coinFlip():
    "Flip a coin"
    if randint(0, 1):
        coin = "Heads"
    else:
        coin = "Tails"
    return coin

# Run the program...
for flip in range(10):
    print(coinFlip())
