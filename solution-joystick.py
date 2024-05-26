#start with imports, ie: import the wrapper
import TMMC_Wrapper
import rclpy
import numpy as np
import math
from ultralytics import YOLO

from utils import collision_detection, stop_sign_detection

model = YOLO("yolov8n.pt")

#start ros
if not rclpy.ok():
    rclpy.init()

TMMC_Wrapper.is_SIM = True
if not TMMC_Wrapper.is_SIM:
    #specify hardware api
    TMMC_Wrapper.use_hardware()
    
if not "robot" in globals():
    robot = TMMC_Wrapper.Robot()

#debug messaging 
print("running main") 
robot.start_keyboard_control() 

#this one is just pure keyboard control

print("start spin once")
rclpy.spin_once(robot, timeout_sec=0.1)

#run the keyboard control functions
print("Begin")
try:
    print("Listening for keyboard events. Press keys to test, Ctrl C to exit")
    while True:
        rclpy.spin_once(robot, timeout_sec=0.1)

        robot.checkScan()
        result = robot.lidar_data_too_close(robot.last_scan_msg, 45*(math.pi/180), -45*(math.pi/180), 0.4)
        print("Close lidar data points:", result)

        print("Collision detection")
        collision_detection(result, robot)

        print("Stop sign detection")
        stop_sign_detection(model, robot)

except KeyboardInterrupt:
    print("keyboard interrupt receieved.Stopping...")
finally:
    #when exiting program, run the kill processes
    robot.stop_keyboard_control()
    robot.destroy_node()
    rclpy.shutdown()


