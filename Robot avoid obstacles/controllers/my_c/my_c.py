"""4_wheel_Robot_controller controller."""

# You may need to import some classes of the controller module. Ex:
from controller import Robot, Motor, DistanceSensor

TIME_STEP = 64

MAX_SPEED = 6.28
# create the Robot instance.
robot = Robot()
    
ps = []

psNames = ['FRsensor','FLsensor']

for i in range (2):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)



bLeftMotor = robot.getDevice('BLmotor')
bRightMotor = robot.getDevice('BRmotor')
fLeftMotor = robot.getDevice('FLmotor')
fRightMotor = robot.getDevice('FRmotor')


bLeftMotor.setPosition(float('inf'))
bRightMotor.setPosition(float('inf'))
fLeftMotor.setPosition(float('inf'))
fRightMotor.setPosition(float('inf'))


bLeftMotor.setVelocity(0.0)
bRightMotor.setVelocity(0.0)
fLeftMotor.setVelocity(0.0)
fRightMotor.setVelocity(0.0)




# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors Values:

    psValues = []
    for i in range (2):
        psValues.append(ps[i].getValue())
    
    
    right_obstacle = psValues[0] < 1000
    left_obstacle = psValues[1] < 1000
    
    
    
    
    
    
    bleftSpeed = 0.5 * MAX_SPEED
    brightSpeed = 0.5 * MAX_SPEED
    fleftSpeed = 0.5 * MAX_SPEED
    frightSpeed = 0.5 * MAX_SPEED


     
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

        
    bLeftMotor.setVelocity(bleftSpeed)
    bRightMotor.setVelocity(brightSpeed)
    fLeftMotor.setVelocity(fleftSpeed)
    fRightMotor.setVelocity(frightSpeed)
