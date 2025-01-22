"""
CSE 2130: Files & File Structures
Reading Text Files
"""


# Complete this function only...

def compare(file1, file2):
    pass


# DO NOT EDIT any of the code below.

def main():
    prompt = "Enter the path to a text file: "
    file1 = input(prompt)
    file2 = input(prompt)
    same = compare(file1, file2)
    print("The files are {} the same.".format("" if same else "NOT"))

main()
