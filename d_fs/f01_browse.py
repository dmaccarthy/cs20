"""
CSE 2130: Files & File Structures
File Systems
"""

# Complete these functions only...

def cwdInfo():
    "Get CWD path and contents from the file system"
    info = {"cwd": None, "files": None, "folders": None}
    return info

def display(info):
    "Display folder info in user-friendly manner"
    print(info)

def runAction(action, info):
    "Respond to user input"
    pass


# DO NOT EDIT any of the code below.

def main():
    action = True
    while action:
        info = cwdInfo()
        display(info)
        print(
            "Type a number to open one of these folders, or type a different path."
        )
        action = input("Type ENTER to quit\n>> ")
        if action: runAction(action, info)

main()
