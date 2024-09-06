"""
CSE 2110: Procedural Programming
Variable Scope
Example 1

"""

from math import sqrt

def pythag_hyp(a, b):
    "Calculate hypotenuse using Pythagoras"
    c = sqrt(a * a + b * b)
    return c

x = 3.0
y = 4.0
z = pythag_hyp(x, y)
print(z)
print(c)