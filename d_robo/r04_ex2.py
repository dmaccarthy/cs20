"""
CSE 1240: Robotics Programming
Colours & Sensors
Example 2

"""

from sc8pr.robot.arena import Arena, quilt
from sc8pr.misc.hsv import hsvBox

def isBlue(color):
    # Check if a color is blue
    return hsvBox(color, (205, 260), (60, 100), (60, 100))

def brain(robot):
    robot.motors = 0.5, 0.3
    while robot.active:
        robot.updateSensors()
        color = robot.sensorDown
        print("\nRGBA =", color)
        print("HSVA =", color.hsva)
        print("Blue =", isBlue(color))

Arena.run(brain, pattern=quilt)
