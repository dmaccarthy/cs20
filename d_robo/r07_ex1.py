"""
CSE 1240: Robotics Programming
Parking Lot Challenge
Example 1

"""

from sc8pr.robot.park import ParkingLot

def brain(robot):
    robot.gyroSample(3)
    robot.motors = 0.5, -0.5
    while robot.active:
        robot.updateSensors()
        print(robot.gyroChange)

ParkingLot.run(brain)
