"""
CSE 2110: Procedural Programming
Pre- & Post-Conditions

"""

# Complete this function.

def salesTax(*args):
    return 0


# Test the function with good and bad data here...

# print(salesTax("a"))

# DO NOT EDIT any of the code below.


def main():
    # Input...
    cost = float(input("Price of item? "))
    rate = float(input("Sales tax as %? ")) / 100

    # Processing...
    tax = salesTax(cost, rate)
    total = cost + tax

    # Output...
    print("Sales Tax: {:.2f}".format(tax))
    print("Total: {:.2f}".format(total))


main()
