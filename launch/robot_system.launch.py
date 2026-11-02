#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
def launch_setup(context):
    mode = LaunchConfiguration('mode').perform(context)
    node_name = LaunchConfiguration('node_name').perform(context)
    listener_name = LaunchConfiguration('listener_name').perform(context)
    topic_override = LaunchConfiguration('topic_name').perform(context)
    overflow_topic = LaunchConfiguration('overflow_topic').perform(context)
    if mode == 'fast':
        publish_rate = 20.0
        max_number = 50
        default_topic = '/even_numbers_fast'
    elif mode == 'slow':
        publish_rate = 5.0
        max_number = 150
        default_topic = '/even_numbers_slow'
    else:
        raise ValueError(
            f"Неизвестный режим '{mode}'. Используйте fast или slow."
        )
    topic_name = topic_override if topic_override else default_topic
    return [
        Node(
            package='m1k_ros_26',
            executable='even_number_publisher',
            name=node_name,
            parameters=[{
                'publish_rate': publish_rate,
                'max_number': max_number,
                'topic_name': topic_name
            }],
            remappings=[
                ('overflow', overflow_topic)
            ],
            output='screen'
        ),
        Node(
            package='m1k_ros_26',
            executable='overflow_listener',
            name=listener_name,
            remappings=[
                ('overflow', overflow_topic)
            ],
            output='screen'
        )
    ]
def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'mode',
            default_value='slow',
            description='Режим работы: fast или slow'
        ),
        DeclareLaunchArgument(
            'node_name',
            default_value='even_number_publisher',
            description='Имя узла публикации'
        ),
        DeclareLaunchArgument(
            'listener_name',
            default_value='overflow_listener',
            description='Имя узла обработки переполнения'
        ),
        DeclareLaunchArgument(
            'topic_name',
            default_value='',
            description='Название топика чётных чисел'
        ),
        DeclareLaunchArgument(
            'overflow_topic',
            default_value='/overflow',
            description=
            'Название топика переполнения'
        ),
        OpaqueFunction(function=launch_setup)
    ])