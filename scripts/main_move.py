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

    def go_2(self):
        global joint_values

        self.setup()
        print("GO!!")
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-35), math.radians(-90)] #角度指定部
        self.setup2(1.3, 100.0, 1)

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
        self.setup2(1.0, 100.0, 1)

        self.setup()        
        joint_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #角度指定部
        self.setup2(1.0, 100.0, 1)

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
        print("search!")
        arm_joint_trajectory_example.go_2()

if __name__ == "__main__":
    rospy.init_node("nagi_uda")
    main()
    rospy.spin()