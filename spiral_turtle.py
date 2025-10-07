#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpiralDrawer(Node):
    def __init__(self):
        super().__init__('spiral_drawer')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.spiral_step)
        self.linear_speed = 0.5
        self.angular_speed = 1.0
        self.step = 0

    def spiral_step(self):
        twist = Twist()
        # Spiral: increase linear speed, keep angular speed constant
        twist.linear.x = self.linear_speed + 0.02 * self.step
        twist.angular.z = self.angular_speed
        self.publisher_.publish(twist)
        self.step += 1
        if self.step > 250:
            twist = Twist()  # Stop after enough steps
            self.publisher_.publish(twist)
            self.get_logger().info("Spiral complete.")
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = SpiralDrawer()
    print("Drawing a spiral with turtle1...")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()