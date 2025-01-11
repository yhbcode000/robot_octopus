cmake_minimum_required(VERSION 3.5)
project(robot_octopus)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find needed packages
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

# For custom messages and services
find_package(rosidl_default_generators REQUIRED)

# Declare the custom messages/services
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/SensorData.msg"
  "msg/ObjectDetection.msg"
  "msg/ControlCommand.msg"
  "srv/PathPlanning.srv"
)

# Export message-related information
ament_export_dependencies(rosidl_default_runtime)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install launch files
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install config files
install(
  DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)

# Install resource files
install(
  DIRECTORY resource/
  DESTINATION share/${PROJECT_NAME}/resource
)

# Install test folder (optional, if you have test assets)
install(
  DIRECTORY test/
  DESTINATION share/${PROJECT_NAME}/test
  FILES_MATCHING PATTERN "*.py"
)

ament_package()
