#include "ros/ros.h"
#include "std_msgs/Int32.h"

void callback(const std_msgs::Int32::ConstPtr& msg){
	ROS_INFO("receive %d", msg->data);
}

int main(int argc, char **argv){
	ros::init(argc, argv, "led_input_listener");
	ros::NodeHandle n;

	ros::Subscriber sub = n.subscribe("led_input", 1, callback);

	ros::spin();

	return 0;
}

