#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
from geometry_msgs.msg import Point, Pose
from gazebo_msgs.msg import ModelStates
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Float32
import message_filters
import os

class SEARCH(object):
    def __init__(self):
        sub_x = message_filters.Subscriber("subscribed_image_color_x", Float32)
        sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
        sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y], 100, 0.1, allow_headerless=True)
        sub_n.registerCallback(self.get)

    def get(self, topic_x, topic_y):
        print(topic_x.data, topic_y.data)
        global robot, arm, flag
        f_x = round((0.1 * topic_x.data) / 150, 4)
        f_y = round((0.1 * topic_y.data) / 150, 4)
        print(f_x, f_y)
        if flag:
            flag = False
            print("GOGO!!")
            setup(0.3, 0.2+f_y, 0.0+f_x, 0.3)#OK
            setup(0.3, 0.2+f_y, 0.0+f_x, 0.1)#OK
            hand(0.1, 0.1)
            os.popen("rosrun crane_x7_ros_test main_move.py")
        else:
            pass
        print("done")

def main():
    global flag, gripper, arm
    flag = True
    gripper = moveit_commander.MoveGroupCommander("gripper")
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_named_target("home")#OK
    arm.go()
    hand(0.5, 0.8)
    setup(0.2, 0.2, 0.0, 0.3)#SET
    search = SEARCH()

def setup(time, x, y, z):
    arm.set_max_velocity_scaling_factor(time)
    arm.set_max_acceleration_scaling_factor(1.0)

    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = x
    target_pose.position.y = y
    target_pose.position.z = z
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴みに行く場合
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

def hand(time, n):
    # ハンド
    gripper.set_joint_value_target([time, n])
    gripper.go()

if __name__ == '__main__':
    rospy.init_node("leo")
    print("OK!!")
    main()
    rospy.spin()
    