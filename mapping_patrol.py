#!/usr/bin/env python

import rospy
import roslib
roslib.load_manifest('my_pkg')
import sys
from std_srvs.srv import Empty, Trigger, TriggerResponse
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import String
from std_msgs.msg import Float32
import tf
import math
import numpy as np
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion





class GoToPose():
    def __init__(self):

        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def navigate(self):
         # Customize the following values so they are appropriate for your location
        position = {'x': 2, 'y' : 0}
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
       
        ###########################################################################
        success = self.goto(position, quaternion)


        
        
        
    
    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'odom'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	# Start moving
        #rospy.loginfo("Go to (%s, %s) pose", pos['x'], quat['y'])
        rospy.loginfo("Go to (%s, %s) pose", pos['x'], pos['y'])
        self.move_base.send_goal(goal)

	# Allow TurtleBot up to 60 seconds to complete task
	success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False

        if result:
            rospy.loginfo("Hooray, reached the desired pose")
        else:
            rospy.loginfo("The base failed to reach the desired pose")

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)       
        
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
        GoToPose()
        GoToPose().navigate() 
       
       
    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")