#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

# BEGIN MEASUREMENT

def scan_callback(msg):
    print("hello")
    
    string=""
    range_center = msg.ranges[len(msg.ranges)/2]
    range_left = msg.ranges[len(msg.ranges)-1]
    range_right = msg.ranges[0]
    string=str(range_center)+"#"+str(range_left)+"#"+str(range_right)
    print(string)
    message_publisher.publish(string)
    
    

#END MEASUREMENT
print("hi")
rospy.init_node('range_ahead',anonymous=True)
scan_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, scan_callback)
message_publisher = rospy.Publisher("messageTopic", String, queue_size=10) 
rospy.spin() 