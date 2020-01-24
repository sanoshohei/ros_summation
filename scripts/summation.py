#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

summation = 0
c = 0

def cb(message):
    # kahan summation
    global summation
    global c
    
    y = message.data - c
    t = summation + y
    c = (t - summation) - y
    summation = t

if __name__ == '__main__':
    rospy.init_node('power')
    sub = rospy.Subscriber('count_up', Float64, cb)
    pub = rospy.Publisher('power', Float64, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()
        pub.publish(summation)
        rospy.loginfo('publish {}'.format(summation))
