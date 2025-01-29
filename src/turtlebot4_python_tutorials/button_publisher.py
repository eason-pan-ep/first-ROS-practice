import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ButtonPublisher(Node):
    def __init__(self):
        super().__init__('button_publisher')
        self.publisher = self.create_publisher(Int32, 'interface_buttons', 10)
        self.timer = self.create_timer(1.0, self.publish_button)
        
    def publish_button(self):
        msg = Int32()
        msg.data = 1  # Simulate a button press
        self.publisher.publish(msg)
        

def main():
    rclpy.init()
    button_publisher = ButtonPublisher()
    rclpy.spin(button_publisher)
    button_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()