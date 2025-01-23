"""
CSE 2130: Files & File Structures
Writing Text Files
"""

# Complete these functions only...

DATA_FILE = ""

def saveData(data, filename):
    pass

def loadData(filename):
    return {}

def editTeam(data, team):
    print(team, data[team])


# DO NOT EDIT any of the code below.

def menu(teams):
    "Display main menu and wait for user input"
    template = "{:4d} - {}"
    n = 1
    print()
    for team in teams:
        print(template.format(n, team))
        n += 1
    print()
    print(template.format(n, "Add Team"))
    print(template.format(0, "Save & Quit"))
    n = None
    while n is None or n < 0 or n > len(teams) + 1:
        try:
            n = int(input("\nSelect a team by number: "))
        except:
            pass
    return n

def main():
    data = loadData(DATA_FILE)
    run = True
    while run:
        teams = sorted(data.keys())
        n = menu(teams)
        if n:
            n -= 1
            if n == len(teams):  # Add team
                name = input("Team name? ")
                data[name] = {"win": 0, "lose": 0, "tie": 0}
                teams.append(name)
            editTeam(data, teams[n])
        else:  # Quit
            run = False
        saveData(data, DATA_FILE)

main()
