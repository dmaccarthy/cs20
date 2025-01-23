"""
CSE 1240: Robotics Programming
Turning the Robot
Example 1

"""

from sc8pr.robot.arena import Arena
from sc8pr.geom import angleDifference

def brain(robot):
    robot.motors = 0.2, -0.2   # Spin in place
    while robot.active:        # Loop until simulation ends
        robot.updateSensors()  # Update the sensor readings
        gyro = robot.gyro      # Get gyro reading
        diff = angleDifference(gyro, 45.0)
        print(f"{gyro:7.2f} {diff:7.2f}")

Arena.run(brain)    # Run the simulation
