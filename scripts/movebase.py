#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *

class Move():

    def __init__(self):

        rospy.init_node('nav', anonymous=False)

        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.goal = MoveBaseGoal()

        self.position_x = []
        self.position_y = []

        self.index = 0

        self.n = int(input("Enter number of goal points : "))

        for i in range(0, self.n):
            self.x = float(input("enter x coordinate"))
            self.y = float(input("enter y coordinate"))

            self.position_x.append(self.x)
            self.position_y.append(self.y)

        self.move_base.wait_for_server()
        rospy.loginfo("waiting for the server")
        
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.header.stamp = rospy.Time.now()
        self.go_to_goal()

    def go_to_goal(self):

        while (self.index<self.n):

            self.goal.target_pose.pose.position.x =  self.position_x[self.index]
            self.goal.target_pose.pose.position.y =  self.position_y[self.index]

            self.goal.target_pose.pose.orientation.w = 1.0 
            
            self.move_base.send_goal(self.goal)

            success = self.move_base.wait_for_result()

            if not success:
                self.move_base.cancel_goal()
                rospy.loginfo("failed to move forward")
            else:
                self.index+=1
                print("moved forward to goal ", str(self.index))   

        print("reached desired goals")        
   

if __name__ == '__main__':
    nav = Move()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Exception")