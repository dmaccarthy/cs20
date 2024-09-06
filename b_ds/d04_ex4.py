"""
CSE 2120: Data Structures
Positional & Keyword Arguments
Example 4

"""

def add(a, b, *args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
    return a + b

name = input("Please enter your name: ")
total = add(1, 2, 3, 4, user=name, year=2021)
print(total)
