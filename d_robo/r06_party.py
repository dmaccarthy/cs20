"""
CSE 1240: Robotics Programming
Lists
Question 3

"""

from sc8pr.robot.party import Party

def brain(robot):
    "Learn the names of the other robots"
    robot.motors = 0.4, 0.3
    while robot.active:
        robot.updateSensors()
        if robot.greet:
            print(robot.greet)

Party.run(brain)
