import rclpy, serial, time, array, re
from datetime import datetime
from rclpy.node import Node

from std_msgs.msg import String, Float32


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_of_weight= self.create_publisher(Float32, 'weight_topic', 10)
        self.publisher_of_time= self.create_publisher(String, 'time_topic', 10)
        self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        try:
            self.port.isOpen()
            print("Serial port is open")
        except:
            print("Serial port is closed")
            exit()
        self.timer_callback()

    def timer_callback(self):
        if(self.port.isOpen()):
            while(1):
                self.raw = self.port.readline().decode()
                self.current_datetime = str(datetime.now())
                if self.raw[0] == "G":
                    self.raw = self.raw[3:-4]
                    self.raw = re.sub(' +',' ',self.raw)
                    self.kg = (int(self.raw) * 0.453592)
                    msg = Float32()
                    msg2 = String()
                    msg.data = self.kg
                    msg2.data = self.current_datetime
                    self.publisher_of_weight.publish(msg)
                    self.get_logger().info("%s" % msg.data)
                    self.publisher_of_time.publish(msg2)
                    self.get_logger().info("%s" % msg2.data)
                
        else:
            print("cannot open serial port")
        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
