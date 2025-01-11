import rclpy
from rclpy.node import Node
from robot_octopus.msg import SensorData

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(SensorData, 'sensor_data', 10)
        self.timer_ = self.create_timer(1.0, self.publish_data)
        self.get_logger().info('SensorNode started.')

    def publish_data(self):
        msg = SensorData()
        msg.temperature = 22.5
        msg.humidity = 45.0
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing sensor data.')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
