#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time
import actionlib
import moveit_commander
import geometry_msgs.msg
from std_msgs.msg import Float64
from std_msgs.msg import Int32, Float32
import message_filters
import rosnode
from tf.transformations import quaternion_from_euler

# Arm communication
from control_msgs.msg import (
    FollowJointTrajectoryAction,
    FollowJointTrajectoryGoal
)
# Gripper communication
from control_msgs.msg import (      
    GripperCommandAction,
    GripperCommandGoal
 )

from trajectory_msgs.msg import JointTrajectoryPoint
import math
import sys
import numpy
import random
import copy

finish = True
global Once_flag_nagi
global SEARCH_MODE

class ArmJointTrajectoryExample(object):
    def __init__(self):
        self._client = actionlib.SimpleActionClient("/crane_x7/arm_controller/follow_joint_trajectory", FollowJointTrajectoryAction)

        rospy.sleep(0.1)
        if not self._client.wait_for_server(rospy.Duration(secs=5)):
            rospy.logerr("Action Server Not Found")
            rospy.signal_shutdown("Action Server Not Found")
            sys.exit(1)

        self.gripper_client = actionlib.SimpleActionClient("/crane_x7/gripper_controller/gripper_cmd",GripperCommandAction)
        self.gripper_goal = GripperCommandGoal()
        self.gripper_client.wait_for_server(rospy.Duration(5.0))
        if not self.gripper_client.wait_for_server(rospy.Duration(5.0)):
            rospy.logerr("Exiting - Gripper Action Server Not Found.")
            rospy.signal_shutdown("Action Server not found.")
            sys.exit(1)
    
    def setup(self):
        global point
        global goal
        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
    def setup2(self, secs2, time, sleep):
        for i, p in enumerate(joint_values):
            point.positions.append(p)
        point.time_from_start = rospy.Duration(secs=secs2)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(time))
        self.gripper_client.send_goal(self.gripper_goal,feedback_cb=self.feedback)
        rospy.sleep(sleep)

    def go(self):
        global joint_values
        #フライ返しの流れ
        self.setup()
        print("SET!!")
        joint_values = [0.0, 0.0, 0.0, 0, 0, 0, 0.0] #角度指定部
        effort  = 1
        self.gripper_goal.command.position = math.radians(20.0)
        self.gripper_goal.command.max_effort = effort
        self.setup2(1.3, 100.0, 1)

        self.setup()
        print("SEARCH!!")      
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-35), math.radians(-90)] #角度指定部
        self.setup2(1.3, 100.0, 1)
        
    def search_mode(self):
        global SEARCH_MODE
        SEARCH_MODE = True
        rate = rospy.Rate(100)
        rate.sleep()
        if SEARCH_MODE:
            sub_x = message_filters.Subscriber("subscribed_image_color_x",Float32)
            sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
            rospy.sleep(0.01)
            n_sub_x = message_filters.Subscriber("subscribed_image_color_x",Float32)
            n_sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
            rate.sleep()
            sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y, n_sub_x, n_sub_y], 10, 0.1, allow_headerless=True)
            sub_n.registerCallback(self.flypan_search)
        else:
            pass

    def flypan_search(self, topic_x, topic_y, n_topic_x, n_topic_y):
        global joint_values
        global Once_flag_nagi
        arm_joint_trajectory_example = ArmJointTrajectoryExample()
        theta = math.degrees(math.atan(topic_y.data / topic_x.data))
        n_x = topic_x.data - n_topic_x.data
        n_y = topic_y.data - n_topic_y.data
        r_x = n_x - topic_x.data
        r_y = n_y

        print("x:", topic_x.data, "y:", topic_y.data, "f", n_topic_x.data, "v", n_topic_y)

        if topic_x.data > -10 and topic_x.data < 10 and topic_y.data > -10 and topic_y.data < 10:
            arm_joint_trajectory_example.go_2()
        elif n_x > -5 and n_x < 5 and n_y > -5 and n_y < 5:
            print("CANCEL!!")
        elif n_x > 30 or n_x < -30 or n_y > 30 or n_y < -30:
            print("ERROR")
        else:
            print("UOOOOOOOOOOOOO")
            self.setup()
            joint_values = [math.radians(theta), math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-35), math.radians(-90 + theta)] #角度指定部
            self.setup2(1.0, 100.0, 0)
            pass


    def go_2(self):
        global joint_values
        self.setup()
        print("PICKUP!!")
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-70), 0.0, math.radians(-80), math.radians(-90)] #角度指定部
        self.setup2(1.3, 100.0, 1)

        self.setup()
        print("UPUP!!")
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-80), math.radians(-90)] #角度指定部
        self.setup2(1.3, 100.0, 0)

        self.setup()
        print("YHAAAAAA!!")
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-30), math.radians(-90)] #角度指定部
        self.setup2(0.2, 100.0, 0)

        self.setup()
        print("YHAA........")
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-75), math.radians(-90)] #角度指定部
        self.setup2(0.2, 100.0, 0)

        self.setup()        
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-35), math.radians(-90)] #角度指定部
        self.setup2(2.0, 100.0, 1)

        return self._client.get_result()

    def feedback(self,msg):
        print("feedback callback")

def main():
    arm_joint_trajectory_example = ArmJointTrajectoryExample()
    global Once_flag_nagi
    global SEARCH_MODE
    Once_flag_nagi = True
    SEARCH_MODE = False
    if Once_flag_nagi:
        Once_flag_nagi = False
        arm_joint_trajectory_example.go()
        print("search!")
        arm_joint_trajectory_example.search_mode()

if __name__ == "__main__":
    rospy.init_node("nagi_uda")
    main()
    rospy.spin()