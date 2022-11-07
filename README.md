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
Then run the following script which will allow you to teleop the bot and generate the entire map of the world
```bash
rosrun vacbot robot_teleop.py
```
Now move the bot using W,A,S,D keys and see the bot generate a beautifull map of the world.

Else you can launch
```bash
roslaunch vacbot robot_offline_nav.launch
```
This will launch Rviz, where you can give 2D goal points to the bot and make it move to the specified point using move-base.
