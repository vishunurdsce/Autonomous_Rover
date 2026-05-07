# 🚀 Viva Prep: Autonomous IMU Rover Project

This guide covers the technical implementation, setup steps, and logic used in your Webots project to help you ace your Viva.

---

### 1. Project Overview
- **Objective**: Build a robot that maintains a stable heading using an IMU, detects dangerous tilts to prevent flipping, and avoids obstacles using IR sensors.
- **Tools**: Webots R2025a (Simulator), Python 3 (Logic).
- **Core Sensors**: `InertialUnit` (IMU), `DistanceSensor` (IR), `Display` (UI).

---

### 1.5 File Structure: Who does What?
- **`worlds/Autonomous_Robot.wbt`**: This is the **Simulation File**. It contains the 3D world, the rocks, the gravity settings (3.71 m/s²), and the robot's physical body.
- **`controllers/imu_controller/imu_controller.py`**: This is the **Brain**. It is the Python script that reads sensor data and tells the motors how fast to spin.
- **`.gitignore`**: A configuration file that tells GitHub to ignore your private viva notes so they stay local to your computer.
- **`VIVA_PREP_GUIDE`**: These are your personal study notes.

---

### 2. The "How-To": Setup & Build Steps

#### 🏗️ Scene Construction
1.  **Arena**: Created using `RectangleArena` (10x10m) with a custom texture to resemble Martian or rugged terrain.
2.  **Obstacles**: Added various `Solid` boxes with `Physics` enabled to test the robot's collision avoidance.

#### 🤖 Robot Architecture
-   **Body**: A `Robot` node with a `Box` geometry for the chassis.
-   **Wheels**: Used 4 `HingeJoints`. 
    -   **Important Setting**: The `anchor` was precisely set (e.g., `0.15 0.17 0`) to ensure the wheels spin on their center axis rather than wobbling.
-   **Sensors**:
    -   **IMU (`InertialUnit`)**: Placed at the center of mass to get accurate Roll, Pitch, and Yaw.
    -   **IR Sensors (`DistanceSensor`)**: Mounted at the front-left and front-right, angled slightly outward.
        -   **Setting Changed**: The `lookupTable` was modified from default to `[0 1024 0, 0.5 0 0]`. This means at 0 meters it returns 1024, and at 0.5 meters it returns 0.

---

### 3. Logic & Control (The Python Brain)

#### 🧭 1. Heading Stabilization (Yaw Control)
-   **The Problem**: Robots often drift due to physics or collisions.
-   **The Solution**: We capture the `target_yaw` on the first step. In every subsequent step, we calculate the `yaw_error` (`target_yaw - current_yaw`).
-   **Proportional Logic**: We adjust wheel speeds based on this error:
    ```python
    correction = 2.0 * yaw_error
    left_speed = base_speed - correction
    right_speed = base_speed + correction
    ```
    *If the robot drifts left, the right wheels speed up to push it back on track.*

#### ⚠️ 2. Tilt Safety (Pitch & Roll)
-   The IMU monitors `roll` and `pitch` values.
-   **Threshold**: If either value exceeds `0.2` radians, the robot **stops immediately**.
-   **Why?** To prevent the rover from flipping over on steep obstacles.

#### 🧱 3. Obstacle Avoidance
-   When `ds_left` or `ds_right` values exceed `100`, the robot enters an **Evasion State**.
-   It performs a **Pivot Turn** (left motors backward, right motors forward) for a set number of steps (`18 steps`) until the path is clear.

---

### 3.5 Detailed Code Walkthrough
Here is what the specific lines in `imu_controller.py` actually mean:

1.  **`robot = Robot()`**: Initializes the Webots API so the code can talk to the simulator.
2.  **`imu.enable(time_step)`**: Crucial step! Sensors are "off" by default to save memory. This "turns on" the IMU.
3.  **`imu.getRollPitchYaw()`**: Returns a list of 3 numbers. We map them to `roll`, `pitch`, and `yaw`.
4.  **`motor.setPosition(float('inf'))`**: Sets the motors to **Velocity Control Mode**. Without this, the motors would only turn to a specific angle and stop.
5.  **`while robot.step(time_step) != -1:`**: The main loop. Everything inside this runs every few milliseconds (the `time_step`).
6.  **`left_val = ds_left.getValue()`**: Reads the Distance Sensor. If it's high (e.g., > 100), something is in front of the robot.
7.  **`display.fillRectangle(...)`**: Updates the virtual screen on the robot. We change the color to **Red** if the robot is tilting, so an engineer knows it's in danger.

---

### 4. Likely Viva Questions

**Q: Why use an IMU for heading instead of just moving the motors at the same speed?**
> *A: Motors are never perfectly matched in physics simulations, and terrain friction causes drift. The IMU provides a "ground truth" orientation, allowing the robot to actively correct its path.*

**Q: How did you implement the Visual UI?**
> *A: I used the `Display` device node. It acts like a small screen on the robot. I used `.drawText()` to overlay real-time Roll/Pitch/Yaw data and a status bar that changes color (Green = Safe, Red = Tilted).*

**Q: What is a lookupTable in the Distance Sensor?**
> *A: It maps physical distance (meters) to the digital value returned by the sensor. I configured it so the value increases as an object gets closer, making it easier to trigger the avoidance logic.*
