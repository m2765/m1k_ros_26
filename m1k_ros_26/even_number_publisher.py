import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'even_numbers', 10)
        self.number = 0
        self.timer = self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        msg = Int32()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Отправлено число: {msg.data}'
        )   
        if self.number >= 2147483646:
            self.number = 0

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