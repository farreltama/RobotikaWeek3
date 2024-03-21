#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

node_name = 'info_listener'

topic_name = 'data_feed'

def on_new_data(received_data):
    rospy.loginfo(f"New data received: {received_data.data}")

rospy.init_node(node_name, anonymous=False)

data_subscriber = rospy.Subscriber(topic_name, Int32, on_new_data)

rospy.spin()
