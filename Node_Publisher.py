#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

node_name = 'info_publisher' 
topic_name = 'info_stream'   

rospy.init_node(node_name, anonymous=False)

info_publisher = rospy.Publisher(topic_name, Int32, queue_size=10) 

publish_rate = rospy.Rate(1) 

message_count = 0 

while not rospy.is_shutdown():
    rospy.loginfo(message_count)
    info_publisher.publish(message_count)
    message_count += 1  # Increment the counter
    publish_rate.sleep() 
