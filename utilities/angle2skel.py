# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:15:00 2015

import numpy as np
import math

def angle2skel(angleArray, meanAngle, arclength):

# ANGLE2SKEL Take in an angle array and integrate over the angles to get
# back a skeleton for each frame.  NB: This reconstruction assumes each 
# segment was equally spaced so that each reconstructed skeleton segment 
# has length arclength/(numAngles + 1)
# 
# Input
#   angleArray - a numSkelPoints - 1 by numFrames array of skeleton
#                tangent angles that have been rotated to have a mean
#                angle of zero.
#   meanAngle  - a 1 by numFrames array of angles.  Each angle is the mean
#                angle of the skeleton used to make the corresponding row
#                of angles in angleArray.  Can be left as zeros if no
#                rotation is desired.
#   arclength  - the total arclength of the skeleton to be reconstructed.
#                Can be set to 1 for a normalised skeleton.
# 
# Output
#   skelX      - a numAngles + 1 by numFrames array of skeleton
#                x-coordinates
#   skelY      - a numAngles + 1 by numFrames array of skeleton
#                y-coordinates

    # get dimensions
    numFrames, numAngles   = np.shape(angleArray)
    
    
    # initialisation
    skelX = np.array([[np.NaN]*(numAngles+1) for i in range(numFrames)])
    skelY = np.array([[np.NaN]*(numAngles+1) for i in range(numFrames)])
    
    for i in range(numFrames):
        
        angle = (angleArray[i] + meanAngle[i])
        cos = np.array([math.cos(i) for i in angle])
        sin = np.array([math.sin(i) for i in angle])
        
        # add up x-contributions of angleArray, rotated by meanAngle
        skelX[i] = np.hstack((np.array(0),np.cumsum(cos)*arclength/(numAngles)))
        # add up y-contributions of angleArray, rotated by meanAngle
        skelY[i] = np.hstack((np.array(0),np.cumsum(sin)*arclength/(numAngles)))
    
    return skelX, skelY
