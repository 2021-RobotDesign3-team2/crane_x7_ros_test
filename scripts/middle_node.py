#!/usr/bin/env python
# -*- conding: utf-8 -*-

import rospy
import message_filters
from std_msgs.msg import Int32, Float32

def main():
    print("OK!!")
    sub_x = message_filters.Subscriber("subscribed_image_color_x",Float32)
    sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
    sub_arm = message_filters.Subscriber("subscribed_arm_status", Float32)
    sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y, sub_arm], 10, 0.1, allow_headerless=True)
    sub_n.registerCallback(search)

def search(topic_x, topic_y, topic_arm):
    print(topic_x.data, topic_y.data, topic_arm.data)
    publisher_x = rospy.Publisher("subscribed_x", Float32)
    publisher_y = rospy.Publisher("subscribed_y", Float32)
    publisher_x.publish(topic_x.data)
    publisher_y.publish(topic_y.data)

if __name__ == "__main__":
    rospy.init_node("middle_node")
    main()
    rospy.spin()
