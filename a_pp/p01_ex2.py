"""
CSE 2110: Procedural Programming
Functions
Example 2

"""

from math import pi

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius**2

def main():
    # Input...
    r = float(input("Radius? "))

    # Processing...
    C = circumference(r)
    A = area(r)

    # Output...
    print("Circumference = {:.2f}".format(C))
    print("Area = {:.2f}".format(A))

main()
