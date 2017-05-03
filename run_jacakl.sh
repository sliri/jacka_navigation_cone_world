#!/bin/bash
killall gzserver
killall -9 gazebo
sleep 8s

mapname=jackal_cone1_world
#create_map=true 
create_map=false 

terminator -e "roslaunch jackal_gazebo $mapname.launch"&
sleep 10s
terminator -e "roslaunch jackal_navigation odom_navigation_demo.launch"&
sleep 10s

if $create_map; then
	sh mybash.sh $mapname
fi
sleep 4s

terminator -e "roslaunch jackal_navigation amcl_demo.launch map_file:=/home/liron/jackal_navigation/src/my_pkg/maps/cone_world1.yaml"&
terminator -e "roslaunch jackal_viz view_robot.launch config:=localization"&
sleep 4s
#terminator -e "rosrun my_pkg cmd_vel_based_patrol.py"&
#sleep 1s
#terminator -e "rosrun my_pkg amcl_subscriber.py"&

#terminator -e "rqt_graph"&
#terminator -e "rqt_plot /amcl_pose/pose/pose/position/x"& 
#terminator -e "rqt_plot /amcl_pose/pose/pose/covariance[1]"& 
#rqt_plot /amcl_pose/pose/pose/covariance[3]& 

#roslaunch jackal_viz view_robot.launch config:=localization
#sleep 5s


#chmod +x navigation.py
#cd ~/catkin_ws
#source ./devel/setup.bash
#catkin_make
#rosrun  image_c navigation.py


#catkin_make
#rosrun  image_c image_c_node&
#gnome-terminal
#cd ~/catkin_ws/src/beginner_tutorials/scripts/
#cd ~/hw2/src/ourpack/src
#chmod +x image_converter.pycd ~/catkin_ws/src/image_c/src
#chmod +x image_converter.cpp
#cd ~/catkin_ws
#source ./devel/setup.bash
#catkin_make
#rosrun  image_c navigation.py
#chmod +x image_converter.cpp
#chmod +x main.cpp
#python turtulebot.py
#roscore
#sleep 10s
#gnome-terminal
#cd ~/catkin_ws
#source ./devel/setup.bash
#rosrun beginner_tutorials image_converter.cpp 
#rosrun beginner_tutorials image_converter.py
#rosrun beginner_tutorials main.cpp liron@ubuntu:~$ cd catkin_ws/
#liron@ubuntu:~/catkin_ws$ source devel/setup.bashliron@ubuntu:~$ cd catkin_ws/

#catkin_ws$ source devel/setup.bash
#rosrun hw2 hw2_node
