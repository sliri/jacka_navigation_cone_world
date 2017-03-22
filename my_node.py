#!/usr/bin/env python

import rospy
import roslib
import sys
from std_srvs.srv import Empty, Trigger, TriggerResponse
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float32
import tf
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class Navigation(object):
    def __init__(self):
    
        # Initialize the node
        rospy.init_node('navigation',anonymous=True)
                
        # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")
       
      

        
        # Subscribe to the odom topic and set 
        # the appropriate callbacks 
        #self.odom_sub = rospy.Subscriber('/jackal_velocity_controller/odom', Odometry, self.odom_callback)
        self.tf_listener = tf.TransformListener()
        
         #initilize  odometry_on  FLAG       
        self.odometry_on=False                  
        #Name of  frames   
        self.frame_id = '/odom'
        self.child_id = '/base_footprint'  
        
       
       
        # Create publisher for cmd_vel topic
        self.pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
        
        
    
    
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    def navigate(self): #sampling rising_edge?  
        self.move_cmd = Twist()
        #self.odom_based_rotate_by_angle(5)    
        #self.cmd_vel.publish(self.move_cmd)
               
        while True:
          
                            
              self.move_cmd.linear.x = 0.5
              self.move_cmd.angular.z = 0.1
              twist_msg = Twist()
              twist_msg.linear.x = 1
              rospy.sleep(1)
              self.pub.publish(twist_msg) 
              print('blalabla')
              self.state_machine()
         
              
              
              
    def state_machine(self):
          self.current_state='linear_move'            
        
        
        
        
        
        
        
        
        
        
       
        


        
def main(args):
     move=Navigation()     
     rospy.init_node('navigation', anonymous=True)
     move.navigate()
     try:
         rospy.spin()
     except KeyboardInterrupt:
          rospy.loginfo("navigation node terminated")
  
if __name__ == '__main__':
    main(sys.argv)



