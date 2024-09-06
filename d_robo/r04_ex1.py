"""
CSE 1240: Robotics Programming
Colours & Sensors
Example 1

"""

from sc8pr.robot.arena import Arena, quilt

def brain(robot):
    robot.motors = 0.5, 0.3
    while robot.active:
        robot.updateSensors()
        print(robot.sensorDown, robot.sensorFront)

Arena.run(brain, pattern=quilt)
