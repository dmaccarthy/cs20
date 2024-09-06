"""
CSE 2120: Data Structures
Generator Functions

"""

# Complete this function only...

def primes(n=None):
    "Generate a sequence of prime numbers"
    yield 2

# DO NOT EDIT any of the code below.

n = int(input("How many numbers? "))
for p in primes(n):
    print(p)
