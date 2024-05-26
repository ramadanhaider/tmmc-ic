import math
import rclpy

def collision_detection(result, robot):
    if result > 0.7:
            robot.stop_keyboard_control()
            robot.send_cmd_vel(0.0, 0.0)
            print("Obstacle just detected, stopping")
            while result > 0.1:
                print("Obstacle detected in while loop, stopping")
                robot.move_backward()
                print("Moving back")
                robot.checkScan()
                result = robot.lidar_data_too_close(robot.last_scan_msg, 45*(math.pi/180), -45*(math.pi/180), 0.2)
                print("Moving back data points:", result)
                rclpy.spin_once(robot, timeout_sec=0.1)
                print("Updated scan")

            robot.send_cmd_vel(0.0, 0.0)
            print("Obstacle cleared, resuming control")
            robot.start_keyboard_control()