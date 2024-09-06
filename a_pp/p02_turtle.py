"""
CSE 2110: Procedural Programming
Variable Scope

"""

from turtle import pencolor, forward, left, exitonclick
from math import pi, sqrt, cos

RADIAN = pi / 180

r = int(input("Radius? "))
n = int(input("How many segments? "))
c = input("Color? ")

pencolor(c)
angle = 360 / n
segment = r * sqrt(2 * (1 - cos(angle * RADIAN)))
while n:
    forward(segment)
    left(angle)
    n -= 1
exitonclick()
