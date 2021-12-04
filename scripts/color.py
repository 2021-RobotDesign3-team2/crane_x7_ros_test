#!/usr/bin/env python
# -*- conding: utf-8 -*-

import sys
import rospy
import numpy as np
import cv2
from rospy.topics import Subscriber
from sensor_msgs import msg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageConvert:
    def __init__(self):
        self.bridge = CvBridge()
        self.subscribed_image_color = rospy.Subscriber("/camera/color/image_raw", Image, self.color_callback_and_convert)

    def main(self):
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("aaaa")
        cv2.destroyAllWindows()

    def color_callback_and_convert(self, topic):
        try:
            cv_image_color = self.bridge.imgmsg_to_cv2(topic, "bgr8")
        except CvBridgeError as e:
            print(e)
        #cv_image_color_2 = cv2.resize(cv_image_color, (640, 360))
        rospy.loginfo('subscribed_image_color')
        self.show(cv_image_color)
        
    def show(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('subscribed_image_color')
    image_convert = ImageConvert()
    image_convert.main()