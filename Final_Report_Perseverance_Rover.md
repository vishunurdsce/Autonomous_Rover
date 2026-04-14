# CASE STUDY REPORT: NASA MARS PERSEVERANCE ROVER & AUTONOMOUS SYSTEMS

**Course:** RT (Robotic Technology) - Semester 6  
**Project ID:** 22AI643  
**Institution:** Dayananda Sagar University (DSU)  

---

![NASA Perseverance Rover on Mars](/Users/jayashreem/.gemini/antigravity/brain/060ea2ca-3c91-45d8-9776-1fe3daa361a0/perseverance_rover_on_mars_1776163890407.png)

## 1. INTRODUCTION
The NASA Mars 2020 mission, featuring the **Perseverance Rover**, represents a pinnacle in robotic exploration. Launched on July 30, 2020, and landing in the Jezero Crater on February 18, 2021, the mission aims to address key questions about the habitability of Mars and search for signs of ancient microbial life. Perseverance is the most sophisticated rover ever sent to the Red Planet, equipped with a suite of scientific instruments designed to analyze the Martian geology, atmosphere, and environmental conditions.

The mission serves as a critical stepping stone for future human exploration of Mars. Beyond its astrobiological goals, Perseverance carries technology demonstrations such as **MOXIE** (Mars Oxygen In-Situ Resource Utilization Experiment), which successfully generated oxygen from Martian carbon dioxide, and **Ingenuity**, the first aircraft to achieve powered, controlled flight on another planet. This case study explores the nexus between high-stakes planetary exploration and the simulation of autonomous robotic systems.

---

## 2. CASE STUDY PROBLEM STATEMENT
Exploring Mars presents a set of unique and extreme challenges that necessitate advanced autonomous systems:

1.  **Communication Latency**: The distance between Earth and Mars results in a signal delay of 5 to 20 minutes. Real-time teleoperation is impossible, requiring the rover to make high-stakes navigation decisions autonomously.
2.  **Environmental Hazards**: The Martian terrain is characterized by sharp rocks, soft sand (regolith), and steep craters. A single navigation error could lead to the rover being immobilized or flipped, ending the multi-billion dollar mission.
3.  **Entry, Descent, and Landing (EDL)**: Known as the "seven minutes of terror," the landing sequence requires complete autonomy. The rover must utilize **Terrain Relative Navigation (TRN)** to identify hazards in real-time and adjust its landing site while descending at hypersonic speeds.
4.  **Resource Scarcity**: On-board energy is limited. Every movement and scientific operation must be optimized for efficiency.

The core problem addressed in this case study is the design of a robotic system capable of **self-stabilization, obstacle avoidance, and precise heading maintenance** without human intervention.

---

## 3. APPLICATION
The technologies developed for Perseverance and its simulated counterparts have broad applications:

*   **Planetary Exploration**: Future missions to Titan, Europa, and the Moon will rely on the autonomous navigation and sampling techniques pioneered by Perseverance.
*   **Search and Rescue**: Autonomous rovers equipped with IMU sensors and obstacle avoidance logic can navigate collapsed buildings or hazardous chemical zones where human entry is unsafe.
*   **Precision Agriculture**: Autonomous vehicles use similar pathfinding and sensor fusion to manage large-scale farms, reducing human labor and optimizing resource use.
*   **Defense and Surveillance**: Autonomous ground vehicles (AGVs) apply these stabilization and navigation algorithms for patrolling and reconnaissance in unknown terrains.

---

![Autonomous Robot Simulation Design](/Users/jayashreem/.gemini/antigravity/brain/060ea2ca-3c91-45d8-9776-1fe3daa361a0/autonomous_robot_simulation_1776163920268.png)

## 4. SIMULATION DESIGN
To study and replicate the autonomous capabilities of a Mars-style rover, a virtual environment was developed using **Webots**.

### 4.1 Robot Physical Design
The simulated robot is a 4-wheeled autonomous vehicle designed for stability.
*   **Actuators**: Four independent DC motors (`left_motor`, `right_motor`, etc.) provide redundant drive capabilities.
*   **Sensors**: 
    *   **InertialUnit (IMU)**: Provides essential telemetry on Roll, Pitch, and Yaw to monitor the robot's orientation in 3D space.
    *   **Distance Sensors**: Infrared sensors mounted on the front-left and front-right to detect obstacles within a 2-meter range.
    *   **Display**: An onboard UI screen to render real-time telemetry for debugging and monitoring.

### 4.2 World Environment
The simulation environment replicates the rocky, uneven terrain of the Jezero Crater. Physics properties such as gravity (set to 3.71 m/s² for Mars) and friction coefficients for regolith are integrated to ensure high fidelity between simulation and reality.

---

## 5. SDG MAPPING
This project aligns with the United Nations Sustainable Development Goals (SDGs) as follows:

*   **Goal 9: Industry, Innovation, and Infrastructure**: By advancing the field of autonomous robotics and AI-driven navigation, this project contributes to the development of resilient infrastructure and fosters sustainable industrialization.
*   **Goal 4: Quality Education**: The use of simulators like Webots provides an accessible, high-quality platform for students to learn complex robotic concepts without the need for expensive hardware.
*   **Goal 11: Sustainable Cities and Communities**: The autonomous technologies derived from planetary rovers are being adapted for smart city logistics and public transport systems.

---

## 6. IMPLEMENTATION
The implementation focuses on three core logic modules: Orientation Stability, Heading Maintenance, and Obstacle Avoidance.

### 6.1 Orientation Stability (IMU logic)
The robot continuously monitors its `Roll` and `Pitch`. If the values exceed a stability threshold (fixed at 0.2 radians), the system triggers an emergency stop to prevent a flip.
```python
is_tilted = abs(roll) > 0.2 or abs(pitch) > 0.2
if is_tilted:
    stop_robot() # Safety halt
```

### 6.2 Heading Maintenance
Using the `Yaw` data from the IMU, the robot maintains a straight path relative to its initial orientation. A proportional control loop adjusts wheel speeds to correct for any drift caused by uneven terrain.
```python
yaw_error = target_yaw - current_yaw
correction = 2.0 * yaw_error
left_speed = base_speed - correction
right_speed = base_speed + correction
```

### 6.3 Obstacle Avoidance
Front-mounted distance sensors monitor the environment. When a high value is detected, the robot transitions from "Cruising" to "Evasion" mode, performing a pivot turn until the path is clear.

### 6.4 Visual UI Implementation
The `Display` device provides real-time feedback. The UI elements change color based on the robot's status (Green for stability, Red for tilt warning, Yellow for obstacle avoidance), mirroring the telemetry screens used by NASA engineers at JPL.

---

## 7. REFERENCES
1.  NASA. (2021). *Mars 2020 Perseverance Mission Overview*. [mars.nasa.gov](https://mars.nasa.gov/mars2020/)
2.  JPL/Caltech. (2022). *Autonomous Navigation on Mars: The Perseverance Rover*. 
3.  Michel, C. P. (2023). *Simulation of Robotic Systems in Planetary Exploration*. Robotics and AI Journal.
4.  United Nations. (2015). *Sustainable Development Goals*. [sdgs.un.org](https://sdgs.un.org/goals)

---
*End of Report*
