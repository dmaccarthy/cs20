"""
CSE 2120: Data Structures
Positional & Keyword Arguments
Example 2

"""

def add(a, b, *args):
    print("Extra:", args)
    return a + b

print(add(1, 2, 3, 4))
