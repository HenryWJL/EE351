#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState


def callback(data):
    global joint_state
    if data is None:
        rospy.logwarn("No joints data!")

    else:
        joint_state = data
      

def main():
    rospy.init_node('jog_command_publisher', anonymous=True)
    rospy.Subscriber('robot_jog_command', JointState, callback, queue_size=10)
    pub = rospy.Publisher('robot_driver/joint_states', JointState, queue_size=10)
    if joint_state is None:
        rospy.logwarn("No joints data!")

    else:
        pub.publish(joint_data)

    rospy.spin()


if __name__ == '__main__':
    joint_state = None
    main()
