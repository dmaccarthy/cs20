"""
CSE 2110: Procedural Programming
Variable Scope

"""

# Predicted output...
#
#
#
#
#

# DO NOT EDIT any of the code below.

def eight():
    global x
    x = 8
    return x

def nine():
    x = 9
    return x

x = 7
print(x)
print(eight())
print(nine())
print(x)
