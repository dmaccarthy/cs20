"""
CSE 2110: Procedural Programming
Exception Handling
Example 2

"""

num1 = float(input("Please enter a number: "))
num2 = float(input("Enter another number: "))
if num2 != 0.0:
    num3 = num1 / num2
    print(f"The quotient of {num1} and {num2} is {num3}.")
else:
    print("Division by zero is undefined!")
