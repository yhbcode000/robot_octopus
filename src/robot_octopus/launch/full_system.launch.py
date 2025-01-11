from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_octopus',
            executable='sensor_node',
            name='sensor_node',
            output='screen'
        ),
        Node(
            package='robot_octopus',
            executable='perception_node',
            name='perception_node',
            output='screen'
        ),
        Node(
            package='robot_octopus',
            executable='planning_node',
            name='planning_node',
            output='screen'
        ),
        Node(
            package='robot_octopus',
            executable='control_node',
            name='control_node',
            output='screen'
        ),
        Node(
            package='robot_octopus',
            executable='actuator_node',
            name='actuator_node',
            output='screen'
        ),
        Node(
            package='robot_octopus',
            executable='system_manager_node',
            name='system_manager_node',
            output='screen'
        ),
    ])
