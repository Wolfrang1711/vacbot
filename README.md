# Vacbot
## A bot which uses LIDAR and designed to map the environment using GMapping

## Installation
### In order to use this package, go through the following steps:

Open you catkin package and go to the src
```bash
cd catkin_ws/src
```
After that clone the repo to your src
```bash
git clone https://github.com/Wolfrang1711/vacbot.git
```
After cloning, source and build the package
```bash
source devel/setup.bash
catkin build
```
## Launching
### In order to launch the package, first launch the gazebo simulation
```bash
roslaunch vacbot robot_gazebo.launch
```
For pre known map based navigation in the environment
```bash
roslaunch vacbot robot_offline_nav.launch
```
This will launch Rviz, which will allow you to visualize the bot in the world and move it to any location using 2D Nav Goals.

For mapping while navigating the environment
```bash
roslaunch vacbot robot_online_nav.launch
```
This will launch Rviz, which will allow you to visualize the bot in the world and map its surroundings dynamically.

For teleoperation of bot to navigate and map surroundings manually
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
Now move the bot using  W,A,S,D keys and see the bot generate a beautiful map of the world.

For autonomous exploration of bot using RRT algorithm to map its surroundings
```bash
rosrun vacbot robot_rrt_explore.py
```
