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
        #self.subscribed_image_depth = rospy.Subscriber("/camera/depth/image_rect_war", Image, self.color_callback_and_convert)

    def main(self):
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("aaaa")
        cv2.destroyAllWindows()

    def color_callback_and_convert(self, msg):
        try:
            cv_image_color = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            #cv_image_depth = self.bridge.imgmsg_to_cv2(msg, "32FC1")

        except CvBridgeError as e:
            print(e)

        rospy.loginfo('subscribed_iimage_color')

        #images = np.hstack((cv_image_color, cv_image_depth))

        #cv2.imshow("Origin Image", images)
        cv2.imshow("Origin Image", cv_image_color)

        #cv2.imshow("depth image", cv_image_depth)
        cv2.waitKey(3)
    
    def depth_callback_and_convert(self, msg):
        try:
            cv_image_depth = self.bridge.imgmsg_to_cv2(msg, "32FC1")
        except CvBridgeError as e:
            print(e)
        
        cv2.imshow("depth image", cv_image_depth)
        cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('subscribed_image_color')
    image_convert = ImageConvert()
    sub = rospy.Subscriber("/bottle_color", Image, image_convert.main)
    image_convert.main()