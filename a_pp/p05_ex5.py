"""
CSE 2110: Procedural Programming
Exception Handling
Example 5

"""

try:
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Enter another number: "))
    num3 = num1 / num2
except ZeroDivisionError:
    print("Division by zero is undefined!")
except ValueError:
    print("Invalid input!")
except Exception as error:
    print("An unknown error occurred...")
    print(type(error), error, sep=": ")
else:
    msg = "The quotient of {} / {} is {}."
    print(msg.format(num1, num2, num3))
