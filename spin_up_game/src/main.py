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

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

drive_x = MotorGroup(motor_1, motor_3)
drive_y = MotorGroup(motor_2, motor_4)

def rotate(x, y):
    deg = math.atan2(y, x)
    r = math.sqrt(y ** 2 + x ** 2)

    # deg in radians

    deg += math.pi / 4

    x = r * math.cos(deg)
    y = r * math.sin(deg)

    return x, y

def parse(axis, velo):
    if velo > 0:
        axis.spin(FORWARD)
    else:
        axis.spin(REVERSE)

    axis.set_velocity(velo, PERCENT)

def drive_mapping():
    while True: # infinite looping or else this check can only run once

        x_pos = controller.axis4.position()
        y_pos = controller.axis3.position()

        isRpressed = controller.buttonR1.pressing() 
        isLpressed = controller.buttonL1.pressing()

        # change turning passed on trigger buttons

        motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, isLpressed)
        motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, isRpressed)
        motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, not isLpressed)
        motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, not isRpressed)

        drive_x = MotorGroup(motor_1, motor_3)
        drive_y = MotorGroup(motor_2, motor_4)

        # convert to polar
        # rotate 45 degrees
        # convert back

        x_pos, y_pos = rotate(x_pos, y_pos)

        if x_pos != 0:
            parse(drive_x, x_pos)
        else:
            drive_x.stop()
        if y_pos != 0:
            parse(drive_y, y_pos)
        else:
            drive_y.stop()

drive_mapping()
