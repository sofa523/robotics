import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from turtlesim.msg import Pose

 
class PoseRelay(Node):
    def __init__(self):

        super().__init__('pose_relay')
        
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            depth=10
        )
        
        self.publisher = self.create_publisher(
            Pose, 'sensor_pose', qos
        )
        self.subscription = self.create_subscription(
            Pose, 'pose', self.callback, 10
        )
    
    def callback(self, msg):
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = PoseRelay()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()