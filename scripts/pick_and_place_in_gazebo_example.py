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
from std_msgs.msg import Int32

global Once_flag_leo

def setup(time, x, y, z):
    global gripper, arm
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(time)
    arm.set_max_acceleration_scaling_factor(1.0)
    gripper = moveit_commander.MoveGroupCommander("gripper")

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
    # 何かを掴んでいた時のためにハンドを開く
    gripper.set_joint_value_target([time, n])
    gripper.go()



def main():
    global robot
    robot = moveit_commander.RobotCommander()

    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    setup(0.5, 0.9, 0.0, 0.3)
    print("GOGO!!")

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:", arm_initial_pose)

    hand(0.1, 0.9)

    # SRDFに定義されている"home"の姿勢にする
    arm.set_named_target("home")
    arm.go()

    # ハンドを開く
    hand(0.7, 0.7)

    # 掴みに行く
    setup(0.5, 0.2, 0.0, 0.13)

    # ハンドを閉じる
    hand(0.4, 0.4)

    # 持ち上げる
    setup(0.5, 0.2, 0.0, 0.3)

    # SRDFに定義されている"home"の姿勢にする
    arm.set_named_target("home")
    arm.go()

    print("done")

if __name__ == '__main__':
    Once_flag_leo = True
    rospy.init_node("leo")
    main()
    #SUB =rospy.SubscribeListener("activate_node", Int32,sub,queue_size=1)
    rospy.spin()
    