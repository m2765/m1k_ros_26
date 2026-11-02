import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool
class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_number_publisher')
        self.declare_parameter('publish_rate', 1.0)
        self.declare_parameter('max_number', 2147483646)
        self.declare_parameter('topic_name', 'ever_number')
        self.publish_rate = self.get_parameter('publish_rate').value
        self.max_number = self.get_parameter('max_number').value
        self.topic_name = self.get_parameter('topic_name').value
        self.publisher_ = self.create_publisher(Int32, self.topic_name, 10)
        self.overflow_publisher = self.create_publisher(Bool, 'overflow', 10)
        self.number = 0
        self.timer = self.create_timer(1.0 / self.publish_rate, self.timer_callback)
    def timer_callback(self):
        msg = Int32()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Отправлено число: {msg.data}'
        )   
        if self.number >= self.max_number:
            self.number = 0

            overflow_msg = Bool()
            overflow_msg.data = True
            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().info('Счётчик сброшен')
        else:
            self.number += 2
def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
if __name__ == '__main__':
    main()