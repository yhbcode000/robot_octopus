#!/bin/bash
# Source the ROS 2 environment (adjust if using a different ROS 2 version)
source /opt/ros/\$ROS_DISTRO/setup.bash

# Build the workspace
colcon build

# Source the workspace
source install/setup.bash
