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
        
        hsv_image = cv2.cvtColor(cv_image_color, cv2.COLOR_BGR2HSV)

        bule_min = np.array([90, 100, 0])
        bule_max = np.array([150, 255, 255])
        flypan_mask = cv2.inRange(hsv_image, bule_min, bule_max)

        cv_image_2 = cv2.bitwise_and(cv_image_color, cv_image_color, mask = flypan_mask)

        gray_image = cv2.cvtColor(cv_image_2, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contours = list(filter(lambda x: cv2.contourArea(x) > 5000, contours))

        cv2.drawContours(hsv_image, contours, -1, color=(0, 0, 255), thickness=6)

        coordinates = cv2.moments(contours[0])
        x = int(coordinates["m10"]/coordinates["m00"])
        y = int(coordinates["m01"]/coordinates["m00"])
        print("x:", x, "y:", y)
        cv2.rectangle(hsv_image, (x + 10, y + 10), (x -10, y - 10), (255, 255, 0), thickness = 6)

        self.show(hsv_image)
        
    def show(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('subscribed_image_color')
    image_convert = ImageConvert()
    image_convert.main()