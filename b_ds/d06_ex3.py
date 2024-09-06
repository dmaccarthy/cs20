"""
CSE 2120: Data Structures
Generator Functions
Example 3

"""

def eulerTerms():
    "Generate the terms of the infinite series for e"
    terms = 0
    nextTerm = 1.0
    while True:  # Loop runs forever!!
        yield nextTerm
        terms += 1
        nextTerm /= terms

def eulerSum():
    "Sum the Euler series until terms become too small to matter"
    euler = 0.0
    for term in eulerTerms():
        prev = euler
        euler += term
        print(term)
        if euler == prev: break
    return euler

print("e =", eulerSum())
