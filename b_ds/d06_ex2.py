"""
CSE 2120: Data Structures
Generator Functions
Example 2

"""

def fib(n):
    "Yield the first n terms of the Fibonacci sequence"
    a = 0
    b = 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

for n in fib(10):
    print(n)
