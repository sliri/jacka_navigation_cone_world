#!/bin/bash
alias mycd='cd ~/jackal_navigation/src/my_pkg/maps/'
mycd
pwd
mapname=$1
echo $mapname
mapname1=$mapname.png
mapname2=$mapname.pgm
#terminator -e "rostopic echo -n 1 /gazebo/model_states > $mapname.txt"& ## big mistake!!!
#==>
terminator -e "rostopic echo -n 1 /gazebo/link_states > $mapname.txt"&
terminator -e "rosrun my_pkg ground_truth1.py $mapname1 $mapname2"&
