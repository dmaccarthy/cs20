"""
CSE 2130: Files & File Structures
Writing Text Files
"""

# Complete these functions only...

def askFileNames():
    "Generate a sequence of file names from user input"
    yield "test.txt"

def appendFile(output, filename, first):
    "Append a text file onto the output file"
    print("Appending {} to {}.".format(filename, output))


# DO NOT EDIT any of the code below.

def main():
    first = True
    output = input("Output file name? ")
    for filename in askFileNames():
        appendFile(output, filename, first)
        first = False

main()
