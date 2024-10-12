import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the TemperatureLogger node
class TemperatureLogger(Node):
    def __init__(self, filename):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(Float32,'/temperature',self.callback,10)
        self.subscription  # prevent unused variable warning
        # self.filename = filename

        # Open the file in append mode
        # self.file = open(self.filename, 'a')

    def callback(self, msg):
        temperature = msg.data
        if temperature > 50.0:
            log_message = f"Temperature above 50°C: {temperature:.2f}\n"
            self.get_logger().info(log_message.strip())
            # self.file.write(log_message)

    # def destroy_node(self):
        # Close the file when the node is destroyed
        # self.file.close()
        # super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
