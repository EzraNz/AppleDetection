#!/usr/bin/env python3

from __future__ import print_function

import rospy
import os
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def talker(images):
    image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
    bridge = CvBridge()
    rospy.init_node('yolov5', anonymous=True)
    i = 0
    
    # while i < len(images):
    #     msg = bridge.cv2_to_imgmsg(images[i], "bgr8")
    #     # rospy.loginfo(msg)
    #     image_pub.publish(msg)
    #     i += 1

    while not rospy.is_shutdown():
        if i == len(images):
            i = 0
        msg = bridge.cv2_to_imgmsg(images[i], "bgr8")
        # rospy.loginfo(msg)
        image_pub.publish(msg)
        i += 1


def main():
    labels = [os.path.join('/home/ekechi/Desktop/Apple_Detection/test', x) for x in os.listdir('/home/ekechi/Desktop/Apple_Detection/test') if x[-4:] == "jpeg"]
    labels.sort()
    labels = np.array(labels)
    images = [cv2.imread(image) for image in labels]

    try:
        talker(images)
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

    