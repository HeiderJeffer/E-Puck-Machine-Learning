
from controller import Robot,DistanceSensor,Motor

TIME_STE=64
MAX_SPEED=6.28
robot = Robot()
ps=[]
psNames=[
    'ps0','ps1','ps2','ps3',
    'ps4','ps5','ps6','ps7'
]
for i in range(8):
    ps.append(robot.getDevice(ps.Names[i]))
    ps[i].enable(TIME_STEP)   
leftMotor=robot.getDevices('left wheel motor')
rightMotor=robot.getDevices('right wheel motor')    
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))
#set the speed to 10 % of the maximum speed
leftmotor.setVelocity(0.0)
rightmotor.setVelocity(0.0)

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    psValues=[]
    for i in range(8):
        psValues.append(ps[i].getValue())

    right_obstacle=psValues[0]>80.0 or psValues[1]>80.0 or psValues[2]>80.0
    left_obstacle=psValues[5]>80.0 or psValues[6]>80.0 or psValues[7]>80.0
    leftSpeed=0.5*MAX_SPPED
    rightSpeed=0.5*MAX_SPPED

    
    if left_obstacle:
        leftSpeed= 0.5*MAX_SPEED
        rightSpeed= -0.5*MAX_SPEED
        
     elif right_obstacle:
            leftSpeed= -0.5 * MAX_SPEED
            rightSpeed= 0.5 * MAX_SPEED   
    
    
    leftMotor.setVelocity(leftSpeed)
    pass


my_new_controller.py
Displaying my_new_controller.py.