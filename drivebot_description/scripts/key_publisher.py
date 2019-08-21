#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Name: key_publisher.py
# Create Date: 09/12/2017
# Edit Date: 03/03/2018
#
# Description:
# ROS node that listens for keystroke and publishes them to the /keystroke topic
# as std_msgs/String messages
#
# Attribution:
# Code example from
# Programming Robots with ROS by Morgan Quigley, Brian Gerkey, and William D. Smart
# (O'Reilly), Chapter 8. Copyright 2015 Morgan Quigley, Brian Gerkey, and William D. Smart,
# 978-1-4493-2389-9.
"""

import sys
import select
import tty
import termios

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    key_publisher = rospy.Publisher('keystroke', String, queue_size=1)
    rospy.init_node("keyboard_driver")
    rate = rospy.Rate(100)
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    print("Publishing keystrokes. Press Ctrl-C to exit...")
    while not rospy.is_shutdown():
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            keypress = sys.stdin.read(1)
            key_publisher.publish(keypress)
            print("Input: " + keypress)
        rate.sleep()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
