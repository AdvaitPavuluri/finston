# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Advait                                                       #
# 	Created:      10/20/2022, 11:50:56 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# TODO: use fleet

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
controller = Controller()

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)

drive_x = MotorGroup(motor_1, motor_2)
drive_y = MotorGroup(motor_3, motor_4)

# Controller button names: https://kb.vex.com/hc/article_attachments/360042385051/5dc33ee3d12f1.jpeg :D

def left_joystick_mapping():
    while True: # infinite looping or else this check can only run once

        x_pos = controller.axis4.position()
        y_pos = controller.axis3.position()

        if x_pos < 0:
            drive_x.spin(REVERSE)
            drive_x.set_velocity(x_pos, PERCENT)
        if x_pos == 0:
            drive_x.stop()
        if x_pos > 0:
            drive_x.spin(FORWARD)
            drive_x.set_velocity(x_pos, PERCENT)
        
        if y_pos < 0:
            drive_x.spin(REVERSE)
            drive_x.set_velocity(y_pos, PERCENT)
        if y_pos == 0:
            drive_x.stop()
        if y_pos > 0:
            drive_x.spin(FORWARD)
            drive_x.set_velocity(y_pos, PERCENT)
        
        # Using only this code might also work:
        # drive_x.set_velocity(x_pos)
        # drive_y.set_velocity(y_pos)
        # But I'm not sure if it'll work because I don't know if making the velocity negative will
        # change the wheels' spin direction

def trigger_mapping():
    while True:
        l2 = controller.buttonL2
        r2 = controller.buttonR2

        # Assume backwards is counterclockwise and forwards is clockwise
        if l2.pressing():
            drive_x.spin(REVERSE)
            drive_y.spin(REVERSE)
        if r2.pressing():
            drive_x.spin(FORWARD)
            drive_y.spin(FORWARD)
    
# TODO: add shooter code, add aimbot, add sensor utils, code autonomous, sigh