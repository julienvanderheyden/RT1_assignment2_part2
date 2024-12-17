# Assignment 2 : ROS2 Part

This package is part of the second assignment for the course **Research Track 1**. It contains a single node, `turtle_controller`, which controls a robot to move in an S-shaped pattern based on its position. 

The node subscribes to the `/odom` topic to get the robot's position and publishes velocity commands on the `/cmd_vel` topic to control the robot's motion according to predefined rules.



---

## Usage

To run the entire simulation, follow these steps:

1. **Launch the simulation environment**:  
   First, launch the Gazebo simulation provided by the [robot_urdf](https://github.com/CarmineD8/robot_urdf) package:
   ```bash
   ros2 launch robot_urdf gazebo.launch.py
   ```

2. **Run the `turtle_controller` node**:  
   Open another terminal and run the controller node from this package:
   ```bash
   ros2 run assignment2_rt_ros2 turtle_controller
   ```

---

## Node Details

### `turtle_controller`

- **Subscribed Topics**:
  - `/odom` (`nav_msgs/msg/Odometry`): Used to retrieve the robot's position and orientation.

- **Published Topics**:
  - `/cmd_vel` (`geometry_msgs/msg/Twist`): Used to send velocity commands to the robot.

- **Behavior**:  
  The robot moves in an S-shaped pattern based on its position (`x`) as follows:
  - If `x > 9.0`, it turns left.
  - If `x < 1.5`, it turns right.
  - Otherwise, it moves straight.

---

## Dependencies

This package requires the following:
- ROS 2 
- [robot_urdf](https://github.com/CarmineD8/robot_urdf) package for simulation.


