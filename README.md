# Reactive Robot Controller for Maze Navigation

## Project Overview

The goal of this project is to design a reactive robot controller using ROS and Gazebo to navigate a maze-like environment. The robot should be able to navigate safely and effectively, avoiding collisions with obstacles and circulating within the maze.

The robot's behavior is based on a reflex-based controller that consists of two sub-behaviors:
- Going straight when no obstacles are present.
- Making turns to avoid collisions with obstacles in its path.

## Features

- Safe Navigation: The robot is designed to avoid collisions with obstacles, ensuring safe movement within the maze.
- Effective Navigation: The robot aims to navigate the maze effectively by continuously circulating in the maze, following a feasible tour path.
- Fast and Smooth Motion: The controller is optimized to provide fast and smooth motion for efficient maze navigation.


![Image 2](https://github.com/shakibaam/Robot-Final/blob/master/maze-like%20scenario.png)


![Image 1](https://github.com/shakibaam/Robot-Final/blob/master/feasible%20maze%20path.png)




## Getting Started

To use this project, follow these steps:

1. Install ROS and Gazebo on your system if you haven't already.

2. Create a new ROS workspace and clone this project into the `src` directory.

3. Build the ROS package using `catkin_make`.

4. Launch the maze simulation environment in Gazebo.

5. Run the `velocity-controller` node to control the robot's movement.

6. Run the `obstacle-detector` node to process sensor data and build the obstacle map.

7. Observe the robot's navigation behavior and monitor its performance in the maze.


