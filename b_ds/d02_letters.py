"""
CSE 2120: Data Structures
Iteration
"""

from sal_ds1.load import load

# Complete these functions only...

def letterFrequency(txt):
    "Determine the frequency of each letter in a sample of text"
    return 26 * [0]

def printResults(freq):
    "Print the frequency table"
    print(freq)


# DO NOT EDIT any of the code below.

def main():
    txt = load(input("File name? "))
    print(txt)
    freq = letterFrequency(txt)
    printResults(freq)

main()
