"""
CSE 2110: Procedural Programming
Exception Handling
Example 6

"""

num = float(input("Enter a positive number: "))
if num <= 0:
    raise ValueError("A positive number is required")
