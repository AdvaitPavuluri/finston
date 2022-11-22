#region VEXcode Generated Robot Configuration
from vex import *

import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Advait                                                       #
# 	Created:      10/20/2022, 11:50:56 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

'''
Front

3 4
1 2

Back

- Forwards: all motors go forward
- Backwards: all motors go backward
- Right: 2 and 3 inverted
- Left: 1 and 4 inverted


'''

# Brain should be defined by default
brain = Brain()
controller = Controller()

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)

#drive_x = MotorGroup(motor_1, motor_2)
#drive_y = MotorGroup(motor_3, motor_4)

def move_all(vel, direction):
    motor_1.spin(direction)
    motor_1.set_velocity(vel, PERCENT)
    motor_2.spin(direction)
    motor_2.set_velocity(vel, PERCENT)
    motor_3.spin(direction)
    motor_3.set_velocity(vel, PERCENT)
    motor_4.spin(direction)
    motor_4.set_velocity(vel, PERCENT)

# Controller button names: https://kb.vex.com/hc/article_attachments/360042385051/5dc33ee3d12f1.jpeg :D

def determine_direction(x, y, num):
    if x > 0 and num in [1,2]:
        return REVERSE
    elif x < 0 and num in [1,3]:
        return REVERSE
    else:
        return FORWARD

def left_joystick_mapping():
    while True:
        x_pos = controller.axis4.position()
        y_pos = controller.axis3.position()
        
        if y_pos != 0:
            motor_1.spin(determine_direction(x_pos, y_pos, 1))
            motor_1.set_velocity(y_pos, PERCENT)
            motor_2.spin(determine_direction(x_pos, y_pos, 2))
            motor_2.set_velocity(x_pos, PERCENT)
            motor_3.spin(determine_direction(x_pos, y_pos, 3))
            motor_3.set_velocity(y_pos, PERCENT)
            motor_4.spin(determine_direction(x_pos, y_pos, 4))
            motor_4.set_velocity(x_pos, PERCENT)
        else:
            motor_1.stop()
            motor_2.stop()
            motor_3.stop()
            motor_4.stop()

# def old_nongigachad_finston_left_joystick_mapping():
#     while True: # infinite looping or else this check can only run once

#         x_pos = controller.axis4.position()
#         y_pos = controller.axis3.position()

#         if x_pos < 0:
#             drive_x.spin(REVERSE)
#             drive_x.set_velocity(x_pos, PERCENT)
#         if x_pos == 0:
#             drive_x.stop()
#         if x_pos > 0:
#             drive_x.spin(FORWARD)
#             drive_x.set_velocity(x_pos, PERCENT)
        
#         if y_pos < 0:
#             drive_y.spin(REVERSE)
#             drive_y.set_velocity(y_pos, PERCENT)
#         if y_pos == 0:
#             drive_y.stop()
#         if y_pos > 0:
#             drive_y.spin(FORWARD)
#             drive_y.set_velocity(y_pos, PERCENT)
        
#         # Using only this code might also work:
#         # drive_x.set_velocity(x_pos)
#         # drive_y.set_velocity(y_pos)
#         # But I'm not sure if it'll work because I don't know if making the velocity negative will
#         # change the wheels' spin direction

# def trigger_mapping():
#     while True:
#         l2 = controller.buttonL2
#         r2 = controller.buttonR2

#         # Assume backwards is counterclockwise and forwards is clockwise
#         if l2.pressing():
#             drive_x.spin(REVERSE)
#             drive_y.spin(REVERSE)
#         if r2.pressing():
#             drive_x.spin(FORWARD)
#             drive_y.spin(FORWARD)

# while True:
#     drive_x.spin(FORWARD)
#     drive_y.spin(FORWARD)

# left_joystick_mapping()
# trigger_mapping()

# TODO: add shooter code, add aimbot, add sensor utils, code autonomous, sigh

def parse(axis, velo):
    if velo > 0:
        axis.spin(FORWARD)
    else:
        axis.spin(REVERSE)

    axis.set_velocity(velo, PERCENT)

# def jacob_has_a_onehundred_incher():
#     while True: # infinite looping or else this check can only run once

#         x_pos = controller.axis4.position()
#         y_pos = controller.axis3.position()

#         # convert to polar
#         # rotate 45 degrees
#         # convert back

#         if x_pos != 0:
#             parse(drive_x, x_pos - 90)
#         else:
#             drive_x.stop()
#         if y_pos != 0:
#             parse(drive_y, y_pos - 90)
#         else:
#             drive_y.stop()

left_joystick_mapping()