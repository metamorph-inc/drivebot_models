cmake_minimum_required(VERSION 2.8.3)
project(drivebot_gazebo)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  drivebot_description
  rqt_gui
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES drivebot_gazebo
#  CATKIN_DEPENDS gazebo_ros joint_state_publisher robot_state_publisher roscpp rospy rviz std_msgs
#  DEPENDS system_lib
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
