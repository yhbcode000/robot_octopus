import rclpy
from rclpy.node import Node
from robot_octopus.srv import PathPlanning

class PlanningNode(Node):
    def __init__(self):
        super().__init__('planning_node')
        self.srv_ = self.create_service(
            PathPlanning,
            'plan_path',
            self.plan_path_callback)
        self.get_logger().info('PlanningNode started.')

    def plan_path_callback(self, request, response):
        self.get_logger().info(f'Received path planning request: {request.start} -> {request.goal}')
        # Here you'd compute a path, fill in response.path
        # We'll skip the actual path for this demo
        return response

def main(args=None):
    rclpy.init(args=args)
    node = PlanningNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
