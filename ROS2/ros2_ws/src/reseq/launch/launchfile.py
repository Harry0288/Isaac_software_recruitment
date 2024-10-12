from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Temperature Sensor
        Node(
            package='reseq',
            executable='temperature_sensor',
            name='temperature_sensor',
            namespace="robot1"
        ),
        # Temperature Logger
        Node(
            package='reseq',
            executable='temperature_logger',
            name='temperature_logger',
            namespace="robot2"
        )
    ])