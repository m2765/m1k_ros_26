#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    params_file = os.path.join(get_package_share_directory('m1k_ros_26'),'params', 'robot_params.yaml')
    return LaunchDescription([Node(package='m1k_ros_26', executable='even_number_publisher', name='even_number_publisher', parameters=[params_file], output='screen'), Node(package='m1k_ros_26', executable='overflow_listener', name='overflow_listener', output ='screen'),])