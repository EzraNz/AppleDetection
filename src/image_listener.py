#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage


def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data)
    file_name = '/home/ekechi/Desktop/Apple_Detection/image/test.jpeg'
    cv2.imwrite(file_name, cv_image)

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('yolov5', anonymous=True)

    # rospy.Subscriber("yolov5/image_out", Image, callback)
    rospy.Subscriber("yolov5/image_out", Image, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()