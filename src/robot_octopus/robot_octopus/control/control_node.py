import rclpy
from rclpy.node import Node
from robot_octopus.msg import ControlCommand

class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        self.publisher_ = self.create_publisher(ControlCommand, 'control_cmd', 10)
        self.timer_ = self.create_timer(0.5, self.publish_command)
        self.get_logger().info('ControlNode started.')

    def publish_command(self):
        cmd = ControlCommand()
        cmd.velocity = 0.5
        cmd.steering_angle = 0.0
        self.publisher_.publish(cmd)
        self.get_logger().info('Publishing control command.')

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
