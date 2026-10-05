import rclpy
import time
from rclpy.node import Node

class TimePrinter(Node):
    def __init__(self):
        super().__init__('timer_printer')
        self.timer = self.create_timer(5.0, self.print_time)

    def print_time(self):
        current_time = time.strftime ('%H:%M:%S', time.localtime())
        self.get_logger().info(f'Текущее время: {current_time}') 

def main(args=None) :
    rclpy.init (args=args)
    node = TimePrinter ()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass 
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ =='__main__':
    main()