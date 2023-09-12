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

Then run the following script which will allow you to teleop the bot and generate the entire map of the world
```bash
rosrun vacbot turtlebot3_teleop.py
```
Now move the bot using W,A,S,D keys and see the bot generate a beautifull map of the world.
