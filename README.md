# Toyota Innovation Challenge: Automated Guided Vehicles (AGVs)

This repository contains the code and resources developed during the **Toyota Innovation Challenge 2024**, where our team tackled the challenge of designing and implementing solutions for Automated Guided Vehicles (AGVs) to navigate a manufacturing environment efficiently and reliably.

---

## 🚀 Project Overview

### Problem Statement
The main goal was to develop an AGV system that:
- **Delivers components** from pickup points to delivery stations.
- **Avoids collisions** with static obstacles, walls, and other AGVs.
- **Obeys traffic signals**, such as stop signs.
- **Minimizes delivery time** in a dynamic manufacturing environment.

### Requirements
Our AGV system was validated through a series of standardized tests, including:
1. **Collision detection** with static fixtures.
2. **Traffic signal recognition** and response.
3. **Autonomous navigation** in dynamic and static obstacle environments.
4. **Fleet control** with multiple AGVs operating simultaneously.

---

## 🧪 Features and Testing Levels

We implemented and tested the AGV system across the following levels:
1. **Keyboard Control with Safety Features**:
   - Manual control with collision detection.
2. **Keyboard Control with Awareness**:
   - Stop sign detection.
3. **Autonomous Control with Static Obstacles**:
   - Fully autonomous navigation avoiding static obstacles and obeying traffic signals.
4. **Autonomous Control with Dynamic Obstacles**:
   - Navigation amidst moving objects (NPCs).
5. **Multi-Agent/Fleet Control**:
   - Coordinated control of multiple AGVs in a shared space.

---

## 🛠️ Technology and Tools

- **Hardware**: TurtleBot robots for real-world testing.
- **Simulation**: Gazebo for validating algorithms in virtual environments.
- **Programming Language**: Python
- **ROS (Robot Operating System)**: For AGV control and integration.
- **OpenCV**: For vision-based traffic signal detection.

---

## 📜 Validation and Results

Our AGV system was rigorously tested across various scenarios and achieved the following results:

- **Collision Detection**: The AGV successfully detected and avoided static obstacles in both simulation and real-world tests.
- **Traffic Signal Recognition**: Stop signs were accurately identified, and the AGV responded by halting appropriately.
- **Autonomous Navigation**: Completed all partial and full courses, navigating efficiently with minimal delivery time.
- **Dynamic Obstacle Avoidance**: Demonstrated reliable performance in environments with moving objects (NPCs).
- **Fleet Control**: Coordinated operation of multiple AGVs without collisions, showcasing efficient multi-agent communication.
