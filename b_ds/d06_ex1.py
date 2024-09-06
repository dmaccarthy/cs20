"""
CSE 2120: Data Structures
Generator Functions
Example 1

"""

def fib(n):
    "Return the first n terms of the Fibonacci sequence"
    a = 0
    b = 1
    fibSeq = []
    while n > 0:
        fibSeq.append(a)
        a, b = b, a + b
        n -= 1
    return fibSeq

for n in fib(10):
    print(n)
