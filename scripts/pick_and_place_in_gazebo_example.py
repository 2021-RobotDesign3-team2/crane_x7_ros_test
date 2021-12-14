#! /usr/bin/env python
# -*- coding: utf-8 -*-

from crane_x7_ros_test.scripts.pose_groupstate_example import SUB, Once_flag_huru
import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Int32

global Once_flag_leo

def setup(time, x, y, z):
    global gripper
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
    # ハンド
    gripper.set_joint_value_target([time, n])
    gripper.go()

def main():
    global robot, arm
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    #SRDFに定義されている"home"の姿勢にする

    print("HHHUUUUUUUUUUU")
    arm.set_named_target("home")#OK
    arm.go()

    print("GOGO!!")
    #setup(0.5, 0.9, 0.0, 0.1)#NG

    # アーム初期ポーズを表示
    #arm_initial_pose = arm.get_current_pose().pose
    #print("Arm initial pose:", arm_initial_pose)

    #hand(0.1, 0.9)
    print("GGAAAAAAAA")
    #setup(0.3, 0.8, 0.0, 0.1)#NG
    print("NPPPPPPPPPPPPP")
    setup(0.3, 0.2, 0.2, 0.3)#OK
    setup(0.3, 0.2, -0.2, 0.3)#OK
    setup(0.3, 0.3, 0.0, 0.1)#OK

    # 開く
    #hand(0.7, 0.7)
    # 掴みに行く
    print("OMMMMMMMMMMMMMMM")
    #setup(0.5, 0.5, 0.0, 0.13)#NG
    #閉じる
    '''
    hand(0.4, 0.4)
    # 持ち上げる
    setup(0.5, 0.2, 0.0, 0.3)
'''
    print("done")

if __name__ == '__main__':
    rospy.init_node("leo")
    print("OK!!")
    main()
    rospy.spin()
