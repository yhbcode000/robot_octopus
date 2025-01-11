from setuptools import setup
import os
from glob import glob

package_name = 'robot_octopus'

setup(
    name=package_name,
    version='0.1.0',
    packages=[
        package_name,
        package_name + '.sensor',
        package_name + '.perception',
        package_name + '.planning',
        package_name + '.control',
        package_name + '.actuator',
        package_name + '.global',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Install config
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        # Install resource
        (os.path.join('share', package_name, 'resource'), glob('resource/*')),
        # Install test files (if any .py)
        (os.path.join('share', package_name, 'test'), glob('test/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='A ROS 2 robot package with subfolders and custom msgs/srvs',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Example entry points for each node:
            'sensor_node = robot_octopus.sensor.sensor_node:main',
            'perception_node = robot_octopus.perception.perception_node:main',
            'planning_node = robot_octopus.planning.planning_node:main',
            'control_node = robot_octopus.control.control_node:main',
            'actuator_node = robot_octopus.actuator.actuator_node:main',
            'system_manager_node = robot_octopus.global.system_manager_node:main',
        ],
    },
)
