import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')

        self.subscription = self.create_subscription(Bool, 'overflow', self.overflow_callback, 10)
        self.get_logger().info('Overflow listener started')
    def overflow_callback(self, msg):
        if msg.data:
            self.get_logger().warning('Counter overflow!')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()

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