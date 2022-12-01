#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
import math

# Begin project code
controller = Controller()

# Ports

# Front
# 3 4
# 2 1
# Back

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

drive_x = MotorGroup(motor_1, motor_3)
drive_y = MotorGroup(motor_2, motor_4)

def rotate(x, y, rotation_angle=math.pi / 4):
    '''
    Converts Cartesian coordinates into polar coordinates, 
    and rotates coordinates around origin by `rotation_angle` radian,
    converts back and returns the rotated Cartesian coordinates
    '''
    deg = math.atan2(y, x)
    r = math.sqrt(y ** 2 + x ** 2)

    # deg in radians

    deg += rotation_angle

    x = r * math.cos(deg)
    y = r * math.sin(deg)

    return x, y

def parse(axis, velo, units=RPM):
    '''
    Changes the axis direction based on the sign of velocity,
    sets the axis velocity to the velocity and units (either `RPM` or `PERCENT`)
    '''
    if velo > 0:
        axis.spin(FORWARD)
    else:
        axis.spin(REVERSE)

    axis.set_velocity(velo, units)

def drive_mapping():
    '''
    Maps the drive to the left joystick omnidirectionally and turning based on triggers
    '''
    while True: 
        # obtain position of joystick in x and y
        x_pos = controller.axis4.position()
        y_pos = controller.axis3.position()
        
        # change turning passed on trigger buttons

        isRpressed = controller.buttonR1.pressing() 
        isLpressed = controller.buttonL1.pressing()
        
        # without turning:
        
        # 3 counterclockwise (true) 4 counterclockwise (true) 
        # 2 clockwise (false)       1 clockwise (false)
        
        # 3 and 4 are different since they are angled differently on the actual robot
        
        # with turning (left):
        
        # 3 clockwise (false) 4 counterclockwise (true) 
        # 2 clockwise (false) 1 counterclockwise (true)
        
        # left side moves in one direction while right side moves in other direction, causing leftward turn
        
        # with turning (right):
        
        # 3 clockwise (true) 4 counterclockwise (false) 
        # 2 clockwise (true) 1 counterclockwise (false)
        
        # same concept but opposite directions causing rightward turning
    
        motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, isLpressed)
        motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, isRpressed)
        motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, not isLpressed)
        motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, not isRpressed)

        # changes direction of motors based on whether it is turning

        drive_x = MotorGroup(motor_1, motor_3)
        drive_y = MotorGroup(motor_2, motor_4)

        x_pos, y_pos = rotate(x_pos, y_pos)
        x_pos, y_pos = x_pos * 5, y_pos * 5 # converts to max of 500 rpm (range is 0 to 500) 
        
        # max of 500 rpm, any more does not seem to make the robot faster but could be tuned further

        # motors cannot seem to interpret a 0 velocity, have to manually stop motors at 0 velocity
        if x_pos != 0:
            parse(drive_x, x_pos)
        else:
            drive_x.stop()
        if y_pos != 0:
            parse(drive_y, y_pos)
        else:
            drive_y.stop()

drive_mapping()
