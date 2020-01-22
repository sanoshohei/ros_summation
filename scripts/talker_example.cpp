#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char **argv){
	ros::init(argc, argv, "led_input_talker");
	ros::NodeHandle n;

	ros::Publisher pub = n.advertise<std_msgs::Int32>("led_input", 1);
	ros::Rate loop_rate(2);

	int input = 0;

	while(ros::ok()){
		std_msgs::Int32 msg;
		msg.data = input;

		pub.publish(msg);
		
		ros::spinOnce();

		loop_rate.sleep();
		input = 1 - input;
	}

	return 0;
}
