import time

def stop_sign_detection(model, robot):
    print("Waiting for image...")
    image_cv2 = robot.rosImg_to_cv2()
    print("Image received")

    stop_sign_detected, x1, y1, x2, y2 = model.ML_predict_stop_sign(model, image_cv2) 
    print ("stop sign detected: ", stop_sign_detected)

    if stop_sign_detected:
        print("Stop sign detected, stopping")
        robot.send_cmd_vel(0.0, 0.0)
        robot.stop_keyboard_control()
        print("Removed keyboard control")
        time.sleep(5)
        robot.start_keyboard_control()
        print("Resumed keyboard control")
        
        while stop_sign_detected:
            print("Still seeing the same stop sign")
            stop_sign_detected, x1, y1, x2, y2 = model.ML_predict_stop_sign(model, image_cv2)

    else: 
        print("No stop sign detected, resuming control")