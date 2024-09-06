"""
CSE 2120: Data Structures
Positional & Keyword Arguments
Example 5

"""

def add(a, b, *args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
    return a + b

total = add(1,2,3, user=name, 4, year=2021)
