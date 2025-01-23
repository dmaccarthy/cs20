"""
CSE 1240: Robotics Programming
Intro to Robotics
Example 1

"""

from sc8pr.robot.arena import Arena

def brain(robot):
    "This function controls the robot"
    robot.pen = "red", 3
    robot.motors = 1

# Run the simulation
Arena.run(brain)    
