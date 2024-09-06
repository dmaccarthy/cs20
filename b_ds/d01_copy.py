"""
CSE 2120: Data Structures
Tuples & Lists

"""

def main():
    "Copy of a list using slices"
    data = list(range(10))
    dataCopy = data
    print(data)
    print(dataCopy)
    assert dataCopy == data, "Lists are not equal"
    assert dataCopy is not data, "List data not copied"


main()
