"""
CSE 1240: Robotics Programming
Functions & Arguments
Example 1

"""

from sc8pr.robot.arena import Arena

def move(robot, time, motors=1):
    "Move the robot for the specified amount of time"
    robot.motors = motors       # Turn motors on
    robot.sleep(time)           # Wait for the specified time
    robot.motors = 0            # Turn motors off
    while not robot.stopped:    # Wait for robot to stop moving
        robot.sleep()

def brain(robot):
    "Robot control function"
    move(robot, 1, -1)          # Move backward for 1 second
    robot.pen = "blue", 3       # Start tracing in blue
    move(robot, 1)              # Move forward for 1 second
    move(robot, 5, (0.7, 0.3))  # Move clockwise for 5 seconds
    move(robot, 2, -1)          # Move backward for 2 seconds

Arena.run(brain)
