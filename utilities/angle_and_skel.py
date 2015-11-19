import numpy as np
import math

#in this script is contained the angle function, the angle to skeleton function(angle2skel)
#and the many angles to many skeletons function(MA2skel). 

def get_true(array):
    indices = [i for i, x in enumerate(array) if x]
    return indices

def angle(val):
    
    x, y = val

    """MAKEANGLEARRAY Get tangent angles for each frame of normBlocks and rotate
                   to have zero mean angle
    
       [ANGLEARRAY, MEANANGLES] = MAKEANGLEARRAY(X, Y)
    
       Input:
           x - the x coordinates of the worm skeleton (equivalent to 
               dataBlock{4}(:,1,:)
           y - the y coordinates of the worm skeleton (equivalent to 
               dataBlock{4}(:,2,:)
    
       Output:
           angleArray - a numFrames by numSkelPoints - 1 array of tangent
                        angles rotated to have mean angle of zero.
           meanAngles - the average angle that was subtracted for each frame
                        of the video."""
    
    
    indices = [j for j in range(len(x)) if np.sum(np.isnan(x[j]))== 0]
    
    x = x[indices]
    y = y[indices]
    
    [numFrames, lengthX] = np.shape(x)
    
    # initialize arrays
    angleArray = np.zeros([numFrames, lengthX-1])
    meanAngles = np.zeros([numFrames,1])
    
    
    for i in range(numFrames):
        # calculate the x and y differences
        dX = np.diff(x[i], n=1, axis=0)
        dY = np.diff(y[i], n=1, axis=0)
        
        # calculate tangent angles.  atan2 uses angles from -pi to pi instead...
        # of atan which uses the range -pi/2 to pi/2.
        angles = np.arctan2(dY, dX)
        #angleArray[i] = angles
        
        # need to deal with cases where angle changes discontinuously from -pi
        # to pi and pi to -pi.  In these cases, subtract 2pi and add 2pi
        # respectively to all remaining points.  This effectively extends the
        # range outside the -pi to pi range.  Everything is re-centred later
        # when we subtract off the mean.
        
        # find discontinuities larger than pi (skeleton cannot change direction
        # more than pi from one segment to the next)
        #1 to cancel diff
        diffs = np.diff(angles, n=1, axis=0)
        #z1 = diffs > 5
        #z2 = diffs < -5
        positiveJumps = np.array(get_true(diffs > 5))+1
        negativeJumps = np.array(get_true(diffs < -5))+1 
        
        # subtract 2pi from remainging data after positive jumps
        if len(positiveJumps>0):
            for j in positiveJumps:
                angles[j:] = angles[j:] - 2*math.pi
        
        # add 2pi to remaining data after negative jumps
        if len(negativeJumps>0):
            for j in negativeJumps:
                angles[j:] = angles[j:] + 2*math.pi
        
        # rotate skeleton angles so that mean orientation is zero
        
        meanAngles[i] = np.mean(angles)
        angles -= meanAngles[i]
        
        # append to angle array
        angleArray[i] = angles
        
    return angleArray, meanAngles

def angle2skel(angle,mean_angle,arclength,numAngles):
    """Input:
        angleArray - a numSkelPoints - 1 by numFrames array of skeleton
                     tangent angles
        mean_angle - the average value of angleArray
        arclength  - the total arc length of the skeleton to be reconstructed
        numAngles  - the length of the angleArray"""

    
    angle = angle + mean_angle

    cos = np.array([math.cos(i) for i in angle])
    sin = np.array([math.sin(i) for i in angle])
    
    # add up x-contributions of angleArray, rotated by meanAngle
    skelX = np.hstack((np.array(0),np.cumsum(cos)*arclength/numAngles))
    # add up y-contributions of angleArray, rotated by meanAngle
    skelY = np.hstack((np.array(0),np.cumsum(sin)*arclength/numAngles))
    
    return skelX, skelY

def MA2skel(angleArray, meanAngle, arclength):

# ANGLE2SKEL integrate over the angles to get back a skeleton for each frame.  
#NB: This reconstruction assumes each segment was equally spaced so that each 
#reconstructed skeleton segment has length arclength/(numAngles + 1)
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
        
        skelX[i],skelY[i]= angle2skel(angleArray[i],meanAngle[i],arclength,numAngles)
    
    return skelX, skelY
