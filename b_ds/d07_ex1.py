"""
CSE 2120: Data Structures
Arrays
Example 1

"""

from array import array

def fib(n):
    "Yield the first n terms of the Fibonacci sequence"
    a = 0
    b = 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

fibTuple = tuple(fib(94))
fibArray = array("Q", fib(94))

print(fibTuple)
print(fibArray)
print(fibArray.itemsize)
