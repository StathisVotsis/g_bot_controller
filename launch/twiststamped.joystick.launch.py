import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='twiststamped_joystick',
            executable='tjoystick.py',
            output='screen',
            arguments=[]),
    ])