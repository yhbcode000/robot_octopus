import rclpy
from rclpy.node import Node
from robot_octopus.msg import SensorData, ObjectDetection

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.subscription_ = self.create_subscription(
            SensorData,
            'sensor_data',
            self.sensor_callback,
            10)
        self.publisher_ = self.create_publisher(ObjectDetection, 'object_detections', 10)
        self.get_logger().info('PerceptionNode started.')

    def sensor_callback(self, msg: SensorData):
        detection = ObjectDetection()
        detection.object_name = "test_object"
        detection.x = 1.0
        detection.y = 2.0
        detection.z = 0.0
        self.publisher_.publish(detection)
        self.get_logger().info('Published detection from sensor data.')

def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
