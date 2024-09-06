"""
CSE 1240: Robotics Programming
Intro to Robotics
Example 3

"""

from sc8pr.robot.arena import Arena

def brain(robot):
    "Spin the robot clockwise"
    robot.pen = "red", 3
    robot.motors = 0.7, -0.7

# Run the simulation
Arena.run(brain)
