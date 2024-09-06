"""
CSE 2110: Procedural Programming
Functions

"""

# Complete these functions only...

def pythag_hyp(a, b):
    pass


def pythag_leg(c, a):
    pass


# DO NOT EDIT any of the code below.


def main():

    # Input...
    a = float(input("Enter one leg: "))
    b = float(input("Enter the other leg: "))

    # Processing...
    c = pythag_hyp(a, b)

    # Output...
    print("The hypotenuse is {}.".format(c))

    # Input...
    c = float(input("Enter the hypotenuse: "))
    a = float(input("Enter one leg: "))

    # Processing...
    b = pythag_leg(c, a)

    # Output...
    print("The other leg is {}.".format(b))


main()
