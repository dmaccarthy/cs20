"""
CSE 2130: Files & File Structures
File Indexing
"""

def readIndex(fn):
    "Return index file and return a list of pointers"
    pass

def getRecord(recNum, data, indx):
    "Retrieve the requested record"
    pass

def main():
    indx = readIndex("resource/ab.indx")
    print("Enter -1 to quit...")
    with open("resources/ab.txt") as data:
        recNum = None
        while recNum != -1:
            recNum = int(input("Record number: "))
            if recNum >= 0:
                print(getRecord(recNum, data, indx))

main()
