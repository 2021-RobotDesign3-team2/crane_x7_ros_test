#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
from geometry_msgs.msg import Point, Pose
from gazebo_msgs.msg import ModelStates
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import geometry_msgs.msg
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Float32
import message_filters
import os

def search():
    global complete
    sub_x = message_filters.Subscriber("subscribed_image_color_x", Float32)
    sub_y = message_filters.Subscriber("subscribed_image_color_y", Float32)
    sub_n = message_filters.ApproximateTimeSynchronizer([sub_x, sub_y], 100, 0.1, allow_headerless=True)
    if complete:
        get(naaa_x, naaa_y)
    else:
        sub_n.registerCallback(get)

def get(topic_x, topic_y):
    global complete
    if complete:
        pass
    else:
        print(topic_x.data, topic_y.data)
        f_x = -1 * round((0.05 * topic_x.data) / 235, 7)
        f_y = -1 * round((0.05 * topic_y.data) / 140, 7)
    global robot, arm, flag, naaa_x, naaa_y
    naaa_x = topic_x.data
    naaa_y = topic_y.data
    print(f_x, f_y)
    if flag:
        complete = True
        flag = False
        setup(0.7, 0.2+f_y, 0.0+f_x, 0.15)#OK
        setup(0.7, 0.2+f_y, 0.0+f_x, 0.11)#OK
        hand(0.25, 1.0)

        os.popen("rosrun crane_x7_ros_test main_move.py")

    print("done")


def main():
    global flag, gripper, arm, complete
    flag = True
    complete = False
    gripper = moveit_commander.MoveGroupCommander("gripper")
    arm = moveit_commander.MoveGroupCommander("arm")
    hand(1.0, 1.0)
    setup(1.0, 0.2, 0.0, 0.3)#SET
    search()

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
    