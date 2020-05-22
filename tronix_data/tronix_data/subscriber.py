import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(Float32,'weight_topic',self.listener_callback_weight,10)
        self.subscription = self.create_subscription(String,'time_topic',self.listener_callback_time,10)
        self.subscription 
    
    def listener_callback_weight(self, msg):
        self.get_logger().info('I heard the weight is: "%s"' % msg.data)
   
    def listener_callback_time(self, msg2):
        self.get_logger().info('I heard the time is: "%s"' % msg2.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

    