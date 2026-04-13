# Autonomous IMU Rover (Webots)

An autonomous robotics simulation built in Webots that utilizes an **Inertial Measurement Unit (IMU)** to achieve highly stable navigation, real-time posture correction, and active obstacle avoidance.

## Core Features
*   **Orientation Monitoring**: Continuously reads Roll, Pitch, and Yaw via the onboard IMU sensor.
*   **Heading Stabilization**: Employs proportional control logic (PID) to maintain a perfectly straight navigational path. If external drift occurs, the robot automatically adjusts its wheel speeds to correct the heading.
*   **Tilt Detection & Safety**: Actively monitors pitch and roll limits. If the robot detects a severe tilt (e.g. driving over extreme terrain), it halts its momentum to physically stabilize and prevent capsizing.
*   **Dynamic Obstacle Avoidance**: Utilizes dual IR distance sensors to detect frontal path blockages. It executes secure pivot evasions and locks into a new stable heading upon clearance.
*   **Live Telemetry UI**: Real-time orientation metrics and environmental status (e.g. 'Maintaining Heading', 'Avoidance Active') are rendered cleanly on the robot's physical digital display, as well as logged to the console.

## Project Structure
*   `worlds/` - Contains the Webots (`.wbt`) environment, complete with the physical robot model, dynamic terrain, and block obstacles.
*   `controllers/imu_controller/` - Houses the Python Brain logic (`imu_controller.py`) handling kinematics, sensor data parsing, and motor velocity control.

## Technology Stack
*   **Simulator**: Webots R2025a
*   **Language**: Python 3
*   **Sensors**: `InertialUnit`, `DistanceSensor` (x2)
*   **Actuators**: `RotationalMotor` (Differential 4-Wheel Drive)

## Getting Started

### Prerequisites
*   [Webots R2025a](https://cyberbotics.com/) installed on your machine.
*   Python 3 configured as the Webots controller language.

### Running the Simulation
1. Launch the Webots application.
2. Click **File -> Open World** and navigate to this repository.
3. Select `worlds/Autonomous_Robot.wbt`.
4. Click **Play** on the simulation toolbar. The robot will automatically spin up its controller and begin navigating the course.
