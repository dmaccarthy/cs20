"""
CSE 1240: Robotics Programming
Intro to Robotics
Example 4

"""

from sc8pr.robot.arena import Arena

def brain(robot):
    "Go forward for 2.5 seconds"
    robot.pen = "red", 3
    robot.motors = 1      # Start both motors
    robot.sleep(2.5)      # Sleep for 2.5 seconds
    robot.motors = 0      # Stop both motors

# Run the simulation
Arena.run(brain)
