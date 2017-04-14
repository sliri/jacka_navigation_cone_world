#!/usr/bin/env python

import matplotlib.pyplot as plt
from collections import Counter
#import rospy
#import roslib
import numpy
from numpy import array
from PIL import Image


##opening the world position file for reading
#world_file = open("world_positions.txt", "r")

#look for the specific objects:
#coounting the number of cloned cones
#see http://stackoverflow.com/questions/38401099/how-to-count-one-specific-word-in-python/38401167
#with open("world_positions.txt") as world_file:
#    contents = world_file.read()
#    cones = contents.count("clone")
#print ("There are %s cones in the world"%cones)

#CONSTANTS
cone_radius=0.2
orchard_length=12
orchard_width=12

#Reading the file and extracting coordinates of the
#objects in the world
coordinates = []                                             #initialize list          
#opening the world position file for reading
with open("world_positions.txt","r") as f:   
    for line in f:
        line = line.split() # to deal with blank        
        if "position:" in line:
          xline=next(f)                                       #next line is "x"         
          [int(s) for s in xline.split() if s.isdigit()]      #extract the numerical value of the coordinate out of rthe text
          x=s
          yline=next(f)                                       #next line is "y"         
          [int(s) for s in yline.split() if s.isdigit()]      #extract the numerical value of the coordinate out of rthe text
          y=s
          coordinates.append((x, y))                          #enter ney coordinate to list       

         
 

# see http://nullege.com/codes/search/matplotlib.pyplot.Circle
#see http://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame

plt.close("all")
fig = plt.figure( dpi=124,figsize=(8,8)) #set image size and DPI are optional
for x in xrange(2,len(coordinates)): #ignoring first 2 coordinates as they are the origin and the jackal locations!
    circlex = plt.Circle(coordinates[x],cone_radius, color='black', linewidth=2,fill=False)
    plt.axis([-orchard_length/2, orchard_length/2, -orchard_width/2, orchard_width/2])
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_artist(circlex)
    ax.set_axis_bgcolor('white')
    ##removing axis and frame
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
 
  
    

    
   
    
#plt.show()
plt.savefig('plotcircles.png')
#converting to pgm see http://code.activestate.com/recipes/577591-conversion-of-pil-image-and-numpy-array/
img = Image.open("plotcircles.png")
arr = array(img)
img = Image.fromarray(arr)
img.save("plotcircles.pgm")




