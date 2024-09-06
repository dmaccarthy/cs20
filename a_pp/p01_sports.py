"""
CSE 2110: Procedural Programming
Functions

"""

# Complete these functions only...

def points(*args):
    return 0


def games_played(*args):
    return 1


# DO NOT EDIT any of the code below.

def main():

    # Input...
    won = int(input("Enter the number of wins: "))
    lost = int(input("Enter the number of regulation losses: "))
    ot = int(input("Enter the number of overtime losses: "))

    # Processing...
    pts = points(won, lost, ot)
    gp = games_played(won, lost, ot)
    ppg = pts / gp

    # Output...
    template = "Your team has {} points and averages {:.2f} points per game in {} games."
    print(template.format(pts, ppg, gp))

main()
