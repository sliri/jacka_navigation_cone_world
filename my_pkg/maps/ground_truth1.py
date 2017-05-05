#!/usr/bin/env python


import matplotlib 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from collections import Counter
#import rospy
#import roslib
import numpy
from numpy import array
from PIL import Image, ImageDraw
import sys
from pylab import *


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

cone_radius=0.1
orchard_length=48   #size of the image in inches. The real size is 40 meter=157.48 inch
orchard_width=48    #size of the image in inches. The real size is 36 meter=141.8732 inch 

#Reading the file and extracting coordinates of the
#objects in the world
coordinates = []                                             #initialize list          
#opening the world position file for reading
with open("jackal_cone1_world.txt","r") as f:   
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
#http://stackoverflow.com/questions/8218608/scipy-savefig-without-frames-axes-only-content

#plt.close("all")
#fig = plt.figure( dpi=100,figsize=(18,20),frameon=False) #set image size and DPI are optional
##for i in xrange(2,len(coordinates)): #ignoring first 2 coordinates as they are the origin and the jackal locations!
#for i in xrange(1,len(coordinates)-1): #ignoring first and last 2 coordinates as they are the origin and the jackal locations!
#    circlex = plt.Circle(coordinates[i],cone_radius, color='black', linewidth=2,fill=False)
#    plt.axis([-orchard_length/2, orchard_length/2, -orchard_width/2, orchard_width/2])
#    fig = plt.gcf()
#    ax = fig.gca()
#    ax.add_artist(circlex)
#    ax.set_axis_bgcolor('white')
#    ##removing axis and frame
#    ax.get_xaxis().set_visible(False)
#    ax.get_yaxis().set_visible(False)
#    ax.spines['top'].set_visible(False)
#    ax.spines['right'].set_visible(False)
#    ax.spines['bottom'].set_visible(False)
#    ax.spines['left'].set_visible(False)
 
  
    


plt.close("all")
fig = plt.figure( dpi=100,figsize=(24,24),frameon=False) #set image size and DPI are optional
#for i in xrange(2,len(coordinates)): #ignoring first 2 coordinates as they are the origin and the jackal locations!
for i in xrange(1,len(coordinates)-1): #ignoring first and last 2 coordinates as they are the origin and the jackal locations!
    circlex = plt.Circle(coordinates[i],cone_radius, color='black', linewidth=2,fill=False)
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
  #  ax.set_aspect('auto')
  



######################################################################
#im = Image.new('RGB', (1800,2000), (255,255,255))
##dr = ImageDraw.Draw(im)
##for i in xrange(1,len(coordinates)-1): #ignoring first and last 2 coordinates as they are the origin and the jackal locations!
##    circlex = plt.Circle(coordinates[i],cone_radius, color='black', linewidth=2,fill=False)
##    dr.ellipse((100,0,50,50), fill="black", outline = "blue")
#
#im.save("circle.png")
#
#
#
#
### Get an example image
#image_file = 'circle.png'
#img = plt.imread(image_file)
#
### Make some example data
### Create a figure. Equal aspect so circles look circular
#fig,ax = plt.subplots(1)
#ax.set_aspect('equal')
##
### Show the image
#ax.imshow(img)
## Now, loop through coord arrays, and create a circle at each x,y pair
#for i in xrange(1,len(coordinates)-1): #ignoring first and last 2 coordinates as they are the origin and the jackal locations!
#    circlex = Circle(coordinates[i],cone_radius, color='black', linewidth=2,fill=False)
#    ax.add_patch(circlex)
###
#### Show the image
##ax.imshow(img)
###im.save("circle.png")
#plt.show()

###########################################    
##plt.show()
#plt.savefig('cone_world.png')
##converting to pgm see http://code.activestate.com/recipes/577591-conversion-of-pil-image-and-numpy-array/
#img = Image.open("cone_world.png")
#arr = array(img)
#img = Image.fromarray(arr)
#img.save("cone_world.pgm")


#plt.show()

try:
    mapname1 = sys.argv[1]
    mapname2 = sys.argv[2]  
except:
    mapname1 = "cone_world.png"
    mapname2 = "cone_world.pgm"
    
    
plt.savefig(mapname1)
#plt.show()

#converting to pgm see http://code.activestate.com/recipes/577591-conversion-of-pil-image-and-numpy-array/
img = Image.open(mapname1)
arr = array(img)
img = Image.fromarray(arr)
img.save(mapname2)

