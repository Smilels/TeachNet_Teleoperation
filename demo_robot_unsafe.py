import rospy
import moveit_commander
from sr_robot_commander.sr_hand_commander import SrHandCommander
from std_msgs.msg import Float64MultiArray

def main():
    rospy.init_node('shadow_unsafe_mode_teleop')
    hand_commander = SrHandCommander(name="right_hand")

    while not rospy.is_shutdown():
        joints_msg = rospy.wait_for_message("/teleop_outputs_joints", Float64MultiArray)
        goal = joints_msg.data

        # bug:get_joints_position() return radian joints
        hand_pos = hand_commander.get_joints_position()

        # first finger
        hand_pos.update({"rh_FFJ3": goal[3]})
        hand_pos.update({"rh_FFJ2": goal[4]})
        hand_pos.update({"rh_FFJ4": goal[2]})

        # middle finger
        hand_pos.update({"rh_MFJ3": goal[12]})
        hand_pos.update({"rh_MFJ2": goal[13]})

        # ring finger
        hand_pos.update({"rh_RFJ3": goal[16]})
        hand_pos.update({"rh_RFJ2": goal[17]})

        # little finger
        hand_pos.update({"rh_LFJ3": goal[8]})
        hand_pos.update({"rh_LFJ2": goal[9]})

        # thumb
        hand_pos.update({"rh_THJ5": goal[19]})
        hand_pos.update({"rh_THJ4": goal[20]})
        hand_pos.update({"rh_THJ3": goal[21]})
        hand_pos.update({"rh_THJ2": goal[22]})

        hand_commander.move_to_joint_value_target_unsafe(hand_pos, 0.3, False, angle_degrees=False)
        rospy.loginfo("Next one please ---->")


if __name__ == "__main__":
    main()
