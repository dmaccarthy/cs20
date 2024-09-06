"""
CSE 2110: Procedural Programming
Variable Scope
Example 4

"""

def test():
    global a
    a = 2
    print(a)

a = 1
test()
print(a)
