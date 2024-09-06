"""
CSE 2110: Procedural Programming
Exception Handling
Example 3

"""

try:
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Enter another number: "))
    num3 = num1 / num2
except ZeroDivisionError:
    print("Division by zero is undefined!")
except ValueError:
    print("Invalid input!")
else:
    print(f"The quotient of {num1} and {num2} is {num3}.")
