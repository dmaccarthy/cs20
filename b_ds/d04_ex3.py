"""
CSE 2120: Data Structures
Positional & Keyword Arguments
Example 3

"""

def add(*args):
    "Calculate the total of an arbitrary number of values"
    total = 0
    for x in args:
        total += x
    return total

print(add(1, 2, 3, 4))
