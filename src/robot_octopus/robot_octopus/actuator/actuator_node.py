import rclpy
from rclpy.node import Node
from robot_octopus.msg import ControlCommand

class ActuatorNode(Node):
    def __init__(self):
        super().__init__('actuator_node')
        self.subscription_ = self.create_subscription(
            ControlCommand,
            'control_cmd',
            self.actuator_callback,
            10)
        self.get_logger().info('ActuatorNode started.')

    def actuator_callback(self, msg: ControlCommand):
        self.get_logger().info(f'Actuator received: velocity={msg.velocity}, steering={msg.steering_angle}')

def main(args=None):
    rclpy.init(args=args)
    node = ActuatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
