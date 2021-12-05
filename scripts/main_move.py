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

    def go(self):
        #フライ返しの流れ
        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, 0.0, 0.0, 0, 0, 0, 0.0] #角度指定部

        effort  = 1.0
        self.gripper_goal.command.position = math.radians(15.0)
        self.gripper_goal.command.max_effort = effort

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=1.3)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)

        self._client.wait_for_result(timeout=rospy.Duration(100.0))
        self.gripper_client.send_goal(self.gripper_goal,feedback_cb=self.feedback)
        rospy.sleep(1)


        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-20), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=1.3)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        rospy.sleep(1)
    
    def search_mode(self):
        #global SEARCH_MODE
        #SEARCH_MODE = True
        sub_x = message_filters.Subscriber("subscribed_image_color_x",Float32)
        sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
        sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y], 10, 0.1, allow_headerless=True)
        sub_n.registerCallback(sub)

    def go_2(self):
        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-70), 0.0, math.radians(-80), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=1.3)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        rospy.sleep(1)
        
        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-80), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=1.3)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-30), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=0.2)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(20), 0.0, math.radians(-115), 0.0, math.radians(-75), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=0.2)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        point = JointTrajectoryPoint()
        goal = FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        joint_values = [0.0, math.radians(-20), 0.0, math.radians(-130), 0.0, math.radians(-35), math.radians(-90)] #角度指定部

        for i, p in enumerate(joint_values):
            point.positions.append(p)
        
        point.time_from_start = rospy.Duration(secs=2.0)
        goal.trajectory.points.append(point)
        self._client.send_goal(goal)
        self._client.wait_for_result(timeout=rospy.Duration(100.0))

        rospy.sleep(1)

        #とりあえず直立
        #point = JointTrajectoryPoint()
        #goal = FollowJointTrajectoryGoal()
        #goal.trajectory.joint_names = ["crane_x7_shoulder_fixed_part_pan_joint","crane_x7_shoulder_revolute_part_tilt_joint","crane_x7_upper_arm_revolute_part_twist_joint","crane_x7_upper_arm_revolute_part_rotate_joint","crane_x7_lower_arm_fixed_part_joint","crane_x7_lower_arm_revolute_part_joint","crane_x7_wrist_joint"]
        
        #joint_values = [0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0] #角度指定部
                
        #for i, p in enumerate(joint_values):
        #    point.positions.append(p)
        
        #point.time_from_start = rospy.Duration(secs=2.0)
        #goal.trajectory.points.append(point)
        #self._client.send_goal(goal)
        #self._client.wait_for_result(timeout=rospy.Duration(100.0))

        #rospy.sleep(1)

        return self._client.get_result()

    def feedback(self,msg):
        print("feedback callback")

def sub(topic_x, topic_y):
    global Once_flag_nagi
    #global SEARCH_MODE
    print("x:", topic_x, "y:", topic_y)
    arm_joint_trajectory_example = ArmJointTrajectoryExample()
    if Once_flag_nagi:
        Once_flag_nagi = False
        #arm_joint_trajectory_example.go()
        print("search!")
        arm_joint_trajectory_example.search_mode()
    #if SEARCH_MODE and topic_x.data > -10 and topic_x.data < 10 and topic_y.data > -10 and topic_y.data < 10:
    #elif Once_flag_nagi and topic_y > 10:
    #    arm_joint_trajectory_example.go_2()

if __name__ == "__main__":
    Once_flag_nagi = True
    SEARCH_MODE = False
    rospy.init_node("nagi_uda")
    print ("gooo")
    sub_x = message_filters.Subscriber("subscribed_image_color_x",Float32)
    sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
    print("hi")
    sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y], 10, 0.1, allow_headerless=True)
    print("hiiiii")
    sub_n.registerCallback(sub)
    #sub(0,0)
    rospy.spin()