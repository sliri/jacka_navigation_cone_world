#!/usr/bin/env python

import rospy
import roslib
roslib.load_manifest('my_pkg')
import sys
from std_srvs.srv import Empty, Trigger, TriggerResponse
from geometry_msgs.msg import Twist ,PoseWithCovarianceStamped
from std_msgs.msg import String
from std_msgs.msg import Float32
import tf
import math
import numpy as np
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import radians
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion



########################################################################
#MAIN EXAMPLE TAKEN FORM
#https://github.com/markwsilliman/turtlebot/blob/master/goforward.py
#########################################################################
class amcl_subscriber():
    def __init__(self):
    
        # Initialize the node
        # rospy.init_node('my_node_name', anonymous=True)#
        # The anonymous keyword argument is mainly used for nodes where
        # you normally expect many of them to be running and
        # don't care about their names (e.g. tools, GUIs)
        #see  http://wiki.ros.org/rospy/Overview/Initialization%20and%20Shutdown       
        rospy.init_node('amcl_subscriber',anonymous=False)
                
        # tell user how to stop TurtleBot and print on Terminal
        rospy.loginfo("To stop Jakcal CTRL + C")
        
        # What function to call when you ctrl + c
        #rospy.on_shutdown(h)
        #Register handler to be called when rospy process begins shutdown.
        #h is a function that takes no arguments. 
        #see http://wiki.ros.org/rospy/Overview/Initialization%20and%20Shutdown
        rospy.on_shutdown(self.shutdown)
             
        
       
        
        # Subscribe to the amcl_pose topic and set 
        # the appropriate callbacks 
        # see http://answers.ros.org/question/49282/amcl-and-laser_scan_matcher/
        # see http://answers.ros.org/question/185907/help-with-some-code-send-a-navigation-goal/
        self.amcl_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.amclPoseCallback)
        
      
       
        
       
        
       
   
        
        
    
       
       
        
        # Publishing rate = 100 Hz look for odometry
        #for sleeping and rate see
        #http://wiki.ros.org/rospy/Overview/Time         
        self.rate = rospy.Rate(10)
       
    
    
    
      
    def run_amcl(self): 
     self.odom_based_linear_move(1) 
    

  
    
 
  
    
             
   
    
        
     
             
             
           

        
    def shutdown(self):
        # stop jackal
        rospy.loginfo("Stop Jackal")
        # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop Jackal
        self.cmd_vel.publish(Twist())
        # sleep just makes sure Jackal receives the stop command prior to shutting down the script
        rospy.sleep(1)



  
          
          
          
          
          
    def amclPoseCallback(self,data):
    #see http://answers.ros.org/question/30227/turtlebot-autonomous-navigation-without-rviz/ 
    #see http://answers.ros.org/question/9686/how-to-programatically-set-the-2d-pose-on-a-map/
    #using http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29
    #using http://wiki.ros.org/navigation/Tutorials/RobotSetup/Odom
    #The nav_msgs/Odometry message stores an estimate of the position and velocity of a robot in free space:  
    #in order to get navigation working you need to publish 2 types of messages. a TF message and an Odomety message.
    #The nav_msgs/Odometry message stores an estimate of the position and velocity of a robot in free space
    #######################################################################################################################        
        #Here, we create a tf.TransformListener object.Once the listener is created, it starts receiving tf transformations
        #over the wire, and buffers them for up to 10 seconds.
        #self.listener = tf.TransformListener()     
        try:
          self.x = data.pose.pose.position.x
          self.y = data.pose.pose.position.y
          self.roll, self.pitch, self.yaw = euler_from_quaternion([data.pose.pose.orientation.x,
                                                    data.pose.pose.orientation.y,
                                                    data.pose.pose.orientation.z,
                                                    data.pose.pose.orientation.w])
          self.covariance = data.pose.covariance 
          rospy.loginfo("Current robot pose: x=" + str(self.x) + "y=" + str(self.y) + " yaw=" + str(math.degrees(self.yaw)) + "Deg")
          rospy.loginfo("Covarianece is " +str(self.covariance))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
          rospy.loginfo("Did not get AMCL data :(")
             
             





        
        
        
   



#I don't undertand the args thing
#Just use it as is        
def main(args):
     amcl_subscriber()     
     rospy.init_node('amcl_subscriber', anonymous=False)
     #amcl_subscriber().run_amcl()
     try:
         rospy.spin()
     except KeyboardInterrupt:
          rospy.loginfo("amcl_subscriber node terminated")
  
if __name__ == '__main__':
    main(sys.argv)


