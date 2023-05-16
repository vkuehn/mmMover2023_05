# ROS2

## config in bashrc

```
source /opt/ros/humble/setup.bash
machine_ip=(`hostname -I`)
export ROS_IP=${machine_ip[0]}
export ROS_DISTRO=humble
echo 'ROS distro:' $ROS_DISTRO
```
