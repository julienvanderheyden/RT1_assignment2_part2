#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('controller')

        # Publisher for velocity commands
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscriber to the robot's odometry
        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        self.get_logger().info('Turtle Controller Node has been started')

    def odom_callback(self, msg):
        # Extract the position from the Odometry message
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        vel = Twist()
        if x > 9.0:
            vel.linear.x = 1.0
            vel.angular.z = 1.0
        elif x < 1.5:
            vel.linear.x = 1.0
            vel.angular.z = -1.0
        else:
            vel.linear.x = 1.0
            vel.angular.z = 0.0

        self.pub.publish(vel)


def main(args=None):
    rclpy.init(args=args)

    # Create and spin the node
    node = TurtleController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # Cleanup
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

