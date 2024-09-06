"""
CSE 2120: Data Structures
Dictionaries & Sets
"""

# NHL Pacific Division standings data

pacific = {
    # Encode data here!
}


# DO NOT EDIT any of the code below.

def main():
    for team, data in pacific.items():
        print(team)
        for v in data.items():
            print("{}: {}".format(*v))
        print()

main()
