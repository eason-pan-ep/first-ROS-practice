"""
This is a practice tutorial project
Goals:
    - Create a ROS2 Python workspace
    - Create a Node class
    - Subscribe to the button topic
    - light up when the button is pressed
"""

from irobot_create_msgs.msg import InterfaceButtons, LightringLeds

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

class TurtleBot4FirstNode(Node):
    def __init__(self):
        super().__init__('turtlebot4_first_python_node')
        
        # Subscribe to the /interface_buttons topic
        self.interface_buttons_subscriber = self.create_subscription(
            InterfaceButtons,
            '/interface_buttons',
            self.interface_buttons_callback,
            qos_profile_sensor_data
        )
        

    def interface_buttons_callback(self, create3_butons_msg: InterfaceButtons):
        # Button 1 is pressed
        if create3_butons_msg.button_1.is_pressed:
            self.get_logger().info('Button 1 Pressed!')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleBot4FirstNode()
    rclpy.spin(node=node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
