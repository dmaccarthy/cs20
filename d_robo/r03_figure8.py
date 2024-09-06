"""
CSE 1240: Robotics Programming
Functions & Arguments
Question 2

"""

from sc8pr.robot.arena import Arena

def circle(robot, motors):
    "Draw a circle"
    angle = robot.gyro
    turnTo(robot, angle + 180, motors)
    turnTo(robot, angle, motors)

def brain(robot):
    "Draw a 'Figure 8'"
    robot.pen = "red", 3
    circle(robot, (0.7, 0.4))
    robot.pen = "blue", 3
    circle(robot, (0.4, 0.7))

Arena.run(brain)
