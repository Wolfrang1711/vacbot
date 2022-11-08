#!/usr/bin/env python

# importing the required modules
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *

# defined a class 'Move'
class Move():

    def __init__(self):

        # initialising a node named 'nav'
        rospy.init_node('nav', anonymous=False)

        # creates the action client 
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        
        # Goal is defined
        self.goal = MoveBaseGoal()

        # assigning a list of goal points
        self.position_x = []
        self.position_y = []

        # declaring that the target goal points will be in the map frame
        self.goal.target_pose.header.frame_id = 'map'

        # to get the current timestamp of the simulation
        self.goal.target_pose.header.stamp = rospy.Time.now()
        
        # initialising the required variables
        self.index = 0

        # taking the user input of the no. of goal points required
        self.n = int(input("Enter number of goal points : "))

        # taking the x and y coordinates of the goal points from the user and storing it in a list
        for i in range(0, self.n):
            self.x = float(input("enter x coordinate"))
            self.y = float(input("enter y coordinate"))

            self.position_x.append(self.x)
            self.position_y.append(self.y)

        # waiting for the action server to start
        self.move_base.wait_for_server()
        rospy.loginfo("waiting for the server")
            
        # calling the go_to_pose() function
        self.go_to_goal()

    def go_to_goal(self):

        # control loop for the bot to move point to point
        while (self.index<self.n):

            # assigning the target x and y coordinates
            self.goal.target_pose.pose.position.x =  self.position_x[self.index]
            self.goal.target_pose.pose.position.y =  self.position_y[self.index]

            # allowing the bot to orient itself as and when required to reach to the goal point
            self.goal.target_pose.pose.orientation.w = 1.0
            
            # sending goal points to the action server
            self.move_base.send_goal(self.goal)

            # waiting for the bot to reach the goal point
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