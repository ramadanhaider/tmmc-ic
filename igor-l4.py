#start with imports, ie: import the wrapper
import TMMC_Wrapper
import rclpy
import numpy as np
import math
import time 

TMMC_Wrapper.is_SIM = True 
#start ros
if not rclpy.ok():
    rclpy.init()

#specify hardware api
TMMC_Wrapper.use_hardware()
if not "robot" in globals():
    robot = TMMC_Wrapper.Robot()

#debug messaging 
print("running main")

#start processes
robot.start_keyboard_control()   #this one is just pure keyboard control
print("starting keyboard control")


print("waiting 10 seconds")


robot.send_cmd_vel(0.1, 0.0)
while True:
    time.sleep(0.5)
    angle1 = 20.0
    angle2 = -20.0
    

    scan = robot.checkScan()
    
    wallDistBig = robot.lidar_data_too_close( scan, angle1*(math.pi/180), angle2*(math.pi/180), 0.8)
    wallDistSmall = robot.lidar_data_too_close( scan, angle1*(math.pi/180), angle2*(math.pi/180), 0.4)
    print("SmallDist: " , wallDistSmall)
    print("BigDist: " , wallDistBig)
    if not wallDistBig > 0.1:
        print("BIG")
        print(wallDistBig)
        robot.send_cmd_vel(0.0, 0.0)
        time.sleep(1)
        robot.rotate( 10.0, 1)
        time.sleep(1)
        robot.send_cmd_vel(0.1, 0.0)
       


    if wallDistSmall > 0.2:
        print("SMALL")
        print(wallDistSmall)
        robot.send_cmd_vel(0.0, 0.0)
        time.sleep(1)
        robot.rotate( 20.0, -1)
        time.sleep(1)
        robot.send_cmd_vel(0.1, 0.0)
    
    



rclpy.spin_once(robot, timeout_sec=0.1)


#run the keyboard control functions
try:
    print("Listening for keyboard events. Press keys to test, Ctrl C to exit")
    while  True: 
        rclpy.spin_once(robot, timeout_sec=0.1)
except KeyboardInterrupt:
    print("keyboard interrupt receieved.Stopping...")
finally:
    #when exiting program, run the kill processes
    robot.stop_keyboard_control()
    robot.destroy_node()
    rclpy.shutdown()