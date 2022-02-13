from AX12 import Ax12
import time 
# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = 'COM8'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 1 
motor_id = 1
my_dxl = Ax12(motor_id)  
my_dxl.set_moving_speed(1023)
time.sleep(0.02)
my_dxl.set_max_torque(1)
time.sleep(0.02)
my_dxl.set_torque_limit(200)
time.sleep(0.02)

def user_input():
    """Check to see if user wants to continue"""
    ans = input('Continue? : y/n ')
    if ans == 'n':
        return False
    else:
        return True

print(f"Max Torque:{my_dxl.get_max_torque()}")
time.sleep(0.1)
print(f"Moving speed: {my_dxl.get_moving_speed()}")
time.sleep(0.1)
print(f"Torque limit: {my_dxl.get_torque_limit()}")
time.sleep(0.1)

def main(motor_object):
    """ sets goal position based on user input """
    bool_test = True

    while bool_test: # bool_test
        # desired angle input
        print(f"\nPosition of dxl ID: {motor_object.id} is {motor_object.get_present_position()} ")
        time.sleep(1)
        input_pos = int(input("goal pos: "))
        motor_object.set_goal_position(input_pos)
        time.sleep(0.1)
        print(f"Position of dxl ID: {motor_object.id} is now: {motor_object.get_present_position()} ")
        time.sleep(0.1)
        bool_test = user_input()       


# pass in AX12 object
main(my_dxl)

# disconnect
my_dxl.set_torque_enable(0)
time.sleep(0.1)
Ax12.disconnect()