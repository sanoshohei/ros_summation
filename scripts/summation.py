#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

summation = 0
c = 0

pub = rospy.Publisher('sum', Float64, queue_size=1)

def cb(message):
    # kahan summation
    global summation
    global c

    global pub
    
    y = message.data - c
    t = summation + y
    c = (t - summation) - y
    summation = t

    pub.publish(summation)
    rospy.loginfo('publish {}'.format(summation))


if __name__ == '__main__':
    rospy.init_node('sum')
    sub = rospy.Subscriber('count_up', Float64, cb)
    rate = rospy.Rate(10)

    rospy.spin()
