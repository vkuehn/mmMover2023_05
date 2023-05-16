Title: ROS2
Date: 2023-10-05 20:30
Modified: 2023-10-05 20:30
Category: Robot
Tags: robot, mmMover
Slug: ros2
Authors: vkuehn
Summary: mm Mover blog

# ROS2

## config in bashrc

```
source /opt/ros/humble/setup.bash
machine_ip=(`hostname -I`)
export ROS_IP=${machine_ip[0]}
export ROS_DISTRO=humble
echo 'ROS distro:' $ROS_DISTRO
```
