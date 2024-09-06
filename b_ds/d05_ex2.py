"""
CSE 2120: Data Structures
List Comprehensions
Example 2

"""

from math import hypot

def distance(p1, p2):
    """Calculate the distance between two points,
    rounded to the nearest whole number"""
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return round(hypot(x, y))

def main():
    invaders = (5, 100), (30, 150), (55, 200), (80, 150), (105, 200)
    player = (300, 620)
    distanceList = [distance(ship, player) for ship in invaders]
    print(distanceList)

main()
