"""
CSE 2110: Procedural Programming
Functions
Example 3

"""

from random import randint

def roll(dice=1, faces=6):
    "Roll one or more dice"
    total = 0
    for i in range(dice):
        total += randint(1, faces)
    return total

print(roll())
print(roll(2, 12))
print(roll(faces=10))
