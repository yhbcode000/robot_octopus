import rclpy
from rclpy.node import Node

class SystemManagerNode(Node):
    def __init__(self):
        super().__init__('system_manager_node')
        self.get_logger().info('SystemManagerNode started.')

def main(args=None):
    rclpy.init(args=args)
    node = SystemManagerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
