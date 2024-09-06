"""
CSE 1240: Robotics Programming
Functions & Arguments
Question 1

"""

from sc8pr.robot.arena import Arena

def turnTo(robot, angle, motors=(0.1, -0.1), accuracy=0.5):
    "Turn the robot until it faces the specified angle"

def brain(robot):
    "Robot control function"
    angle = robot.numinput("Enter a direction")
    turnTo(robot, angle)

Arena.run(brain)