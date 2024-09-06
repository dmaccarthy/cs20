"""
CSE 1240: Robotics Programming
Colours & Sensors
Question 1

"""

from sc8pr.robot.arena import Arena, quilt

def brain(robot):
    turnTo(robot, 290)
    robot.motors = 0.3
    while robot.active:
        robot.updateSensors()
        color = robot.sensorDown
        print(color.hsva)

Arena.run(brain, pattern=quilt)