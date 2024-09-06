"""
CSE 2110: Procedural Programming
Exception Handling
Example 4

"""

try:
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Enter another number: "))
    num3 = num1 / num2
except (ZeroDivisionError, ValueError) as error:
    print(type(error), error)
else:
    msg = "The quotient of {} / {} is {}."
    print(msg.format(num1, num2, num3))
