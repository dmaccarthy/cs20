"""
CSE 1240: Robotics Programming
Intro to Robotics
Example 2

"""

from sc8pr.robot.arena import Arena

def brain(robot):
    "Move the robot clockwise"
    robot.pen = "red", 3
    robot.motors = 0.7, 0.3

# Run the simulation
Arena.run(brain)
