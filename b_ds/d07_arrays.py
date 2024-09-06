"""
CSE 2120: Data Structures
Arrays

"""

# Enter your results here as comments

# Average Generation Time...
# List:
# Array:
# Tuple:

# Average Processing Time...
# List:
# Array:
# Tuple: N/A (Immutable!)

from random import random
from array import array

# Complete these functions only...

def makeArray(n):
    pass


def makeTuple(n):
    pass


# DO NOT EDIT any of the code below.

def makeList(n):
    return [random() for i in range(n)]

from time import time
from math import sqrt

def runTest(makeData, n=1000000):
    t0 = time()
    data = makeData(n)
    t1 = time()
    print("Time to generate {} data: {:.4f} sec".format(
        type(data).__name__, t1 - t0))
    try:
        for i in range(n):
            data[i] = sqrt(data[i])
        t2 = time()
        print("Time to process data: {:.4f} sec".format(t2 - t1))
    except Exception as e:
        print("ERROR!", e)
    print()

def main():
    runTest(makeList)
    runTest(makeArray)
    runTest(makeTuple)

main()
