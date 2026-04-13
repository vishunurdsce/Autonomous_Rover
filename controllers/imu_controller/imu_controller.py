from controller import Robot
import math

def run_robot():
    robot = Robot()
    time_step = int(robot.getBasicTimeStep())
    
    # Initialize Devices
    left_motor = robot.getDevice('left_motor')
    right_motor = robot.getDevice('right_motor')
    left_rear_motor = robot.getDevice('left_rear_motor')
    right_rear_motor = robot.getDevice('right_rear_motor')
    
    motors = [left_motor, right_motor, left_rear_motor, right_rear_motor]
    for motor in motors:
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
    
    imu = robot.getDevice('imu')
    imu.enable(time_step)
    
    display = robot.getDevice('display')
    
    ds_left = robot.getDevice('ds_left')
    ds_right = robot.getDevice('ds_right')
    ds_left.enable(time_step)
    ds_right.enable(time_step)
    
    # Vars
    base_speed = 5.0
    target_yaw = 0.0
    first_step = True
    evasion_timer = 0
    
    display.setFont("Arial", 14, True)

    while robot.step(time_step) != -1:
        # Core Requirement 1: Use InertialUnit sensor to Get Roll, Pitch, Yaw
        rpy = imu.getRollPitchYaw()
        roll = rpy[0]
        pitch = rpy[1]
        yaw = rpy[2]
        
        if first_step:
            target_yaw = yaw
            first_step = False
            
        # Core Requirement 5: Print roll, pitch, yaw continuously
        print(f"[IMU DATA]  Roll: {roll:.3f} | Pitch: {pitch:.3f} | Yaw: {yaw:.3f}")
            
        left_val = ds_left.getValue()
        right_val = ds_right.getValue()
        
        # Core Requirement 3: Detect unwanted tilt (pitch/roll changes)
        is_tilted = abs(roll) > 0.2 or abs(pitch) > 0.2
        
        status_text = "MAINTAINING HEADING"
        
        if is_tilted:
            # Core Requirement 4: Correct motion in real-time -> Adjust speeds to stabilize
            left_speed = 0.0
            right_speed = 0.0
            status_text = "WARNING: UNSTABLE TILT DETECTED"
            print(">>> TILT WARNING! Stopping to prevent flip. <<<")
            
        elif left_val > 100 or right_val > 100 or evasion_timer > 0:
            # Core Requirement 6: Avoid obstacles
            if evasion_timer == 0:
                evasion_timer = 18 # Pivot for 18 steps to safely turn away
            
            status_text = "AVOIDING OBSTACLE"
            # Pivot turn
            left_speed = -base_speed
            right_speed = base_speed
            evasion_timer -= 1
            
            if evasion_timer == 0:
                # Once rotated, set the new safe direction as our target yaw to maintain
                target_yaw = yaw
                
        else:
            # Core Requirement 2: Maintain stable heading -> Move straight / Correct drifting
            yaw_error = target_yaw - yaw
            
            # Normalize error
            while yaw_error > math.pi: yaw_error -= 2 * math.pi
            while yaw_error < -math.pi: yaw_error += 2 * math.pi
            
            # Proportional Control to adjust wheel speeds
            correction = 2.0 * yaw_error
            left_speed = base_speed - correction
            right_speed = base_speed + correction
            
        # Ensure we don't exceed Webots physical limits to avoid warnings
        left_speed = max(min(left_speed, 10), -10)
        right_speed = max(min(right_speed, 10), -10)
        
        # Apply speeds
        left_motor.setVelocity(left_speed)
        left_rear_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        right_rear_motor.setVelocity(right_speed)
        
        # Core Requirement 5: Display orientation values (Visual UI)
        display.setColor(0x1A1A1A) 
        display.fillRectangle(0, 0, display.getWidth(), display.getHeight())
        
        if is_tilted:
            display.setColor(0xFF0000)
        elif evasion_timer > 0:
            display.setColor(0xFFFF00)
        else:
            display.setColor(0x00FF00)
        display.fillRectangle(0, 0, display.getWidth(), 8)
        
        display.setColor(0x00FF00)
        display.drawText(f"ROLL:  {roll:.3f}", 15, 25)
        display.drawText(f"PITCH: {pitch:.3f}", 15, 50)
        display.drawText(f"YAW:   {yaw:.3f}", 15, 75)
        
        display.setColor(0xFFFFFF)
        display.drawText(status_text, 15, 105)

if __name__ == "__main__":
    run_robot()
