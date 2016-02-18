# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:41:55 2015

@author: aidanrocke
"""
#duration_distributions

from behavioral_syntax.utilities.angle_and_skel import angle
from scipy.stats import spearmanr

import numpy as np


def pauses(posture_sequence):
    """ Return the distribution of pauses.

        Input:
            posture_sequence: a sequence of postures

        Output:
            pause_matrix: a 2 dimensional matrix with pauses in the first row and 
                          the respective postures in the second row

        remark: there are no absolute pauses that can be detected with certainty. 
                So we can't say that we have detected pauses unless the raw data
                confirms that. But, we can say that we can detect insignificant 
                movement.
    """
    j = 0
    k = 0

    n = len(posture_sequence)
    pauses = np.zeros((2,round(n/10)))
    most_recent_elem = None
    for i in range(n):
        if posture_sequence[i] == most_recent_elem:
            j+=1
        else:
            pauses[:,k] = posture_sequence[i], j
            most_recent_elem = posture_sequence[i]
            pauses.append(j)
            j=0
            k+=1

    return pauses

def velocity(skeletons):
    """
        This determines the speed and velocity of the worms up to a constant multiple. 

        Input: 
            skeletons: a list of skeletons taken as output from the loading_data function

        Output:
            velocity: a list of velocity arrays
            speed: a list of speed arrays
    """

    speed = []
    velocity = []

    for i in range(len(skeletons)):
        X,Y = skeletons[i]

        C,c = np.shape(X)

        #the midpoint of the skeleton will be used to compute speed and changes in velocity
        mid_point = round(c/2)
        
        speed = np.zeros(C)
        velocity = np.zeros(C)
        
        #compute speed and velocity:
        j =0
        while j<C+1:
            if sum(np.isnan(X[j]))+sum(np.isnan(X[j+1]))== 0:
                norm = np.sqrt(np.linalg.norm(X[j+1][mid_point]-X[j][mid_point])**2+np.linalg.norm(Y[j+1][mid_point]-Y[j][mid_point])**2)
                speed[i] =  norm
                v = np.array([X[j+1][mid_point]-X[j][mid_point],Y[j+1][mid_point]-Y[j][mid_point]])
                velocity[i] = v
            else:
                j+=1
                
        speed.append(speed)
        velocity.append(velocity)

    return speed, velocity

def eigenworm_importance(skeletons):

    N = len(skeletons)

    eig_importance = np.zeros(N)

    for i in range(len(skeletons)):
        X,Y = skeletons[i]

        C,c = np.shape(X)
        
        stat_vec = np.zeros(C)

        angles = angle((X,Y))
        angles = angles[0]

        covar = np.cov(np.transpose(angles))

        eigen, eigenvec = np.linalg.eigh(covar)

        for j in range(C):
            theta = np.zeros(c)

            for k in range(c):
                theta += eigenvec[k]*np.dot(eigenvec[k],angles[k])

            stat_vec[j] = spearmanr(theta,angles[j])[0]

        eig_importance[i] = np.mean(stat_vec)

    return eig_importance
