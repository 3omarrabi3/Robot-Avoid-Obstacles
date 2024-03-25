"""4_wheel_Robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor

TIME_STEP = 64

MAX_SPEED = 6.28
# create the Robot instance.
robot = Robot()

ps = []

psNames = ['ps0', 'ps1']

for i in range(2):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

fLeftMotor = robot.getDevice('Front Left Wheel Motor')
fRightMotor = robot.getDevice('Front Right Wheel Motor')
bLeftMotor = robot.getDevice('Back Left Wheel Motor')
bRightMotor = robot.getDevice('Back Right Wheel Motor')

fLeftMotor.setPosition(float('inf'))
fRightMotor.setPosition(float('inf'))
bLeftMotor.setPosition(float('inf'))
bRightMotor.setPosition(float('inf'))

fLeftMotor.setVelocity(0.0)
fRightMotor.setVelocity(0.0)
bLeftMotor.setVelocity(0.0)
bRightMotor.setVelocity(0.0)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors Values:
    psValues = []
    for i in range(2):
        psValues.append(ps[i].getValues())

    right_obstacle = psValues[0] > 80.0
    left_obstacle = psValues[1] > 80.0

    fleftSpeed = 0.5 * MAX_SPEED
    bleftSpeed = 0.5 * MAX_SPEED

    frightSpeed = 0.5 * MAX_SPEED
    brightSpeed = 0.5 * MAX_SPEED

    if left_obstacle:
        fleftSpeed = 0.5 * MAX_SPEED
        bleftSpeed = 0.5 * MAX_SPEED

        frightSpeed = -0.5 * MAX_SPEED
        brightSpeed = -0.5 * MAX_SPEED

    if right_obstacle:
        fleftSpeed = -0.5 * MAX_SPEED
        bleftSpeed = -0.5 * MAX_SPEED

        frightSpeed = 0.5 * MAX_SPEED
        brightSpeed = 0.5 * MAX_SPEED

    fLeftMotor.setVelocity(fleftSpeed)
    bLeftMotor.setVelocity(bleftSpeed)
    fRightMotor.setVelocity(frightSpeed)
    bRightMotor.setVelocity(brightSpeed)

    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

# Enter here exit cleanup code.
