# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:42:45 2016

@author: aidanrocke
"""

#this is based on the paper: Computational Methods for Tracking, Quantitative 
#Assessment, and Visualization of C. elegans

import numpy as np

#data = source

from behavioral_syntax.loading_data import get_skeletons

#Lévy flight test for foraging behavior in worms off food. 

#visualize distribution of step sizes:
X,Y = get_skeletons(data)

#get step sizes:
mid = int(len(X[0])/2)

#take the distance travelled between every ten frames:
#create step-length array:

S = np.zeros(int(len(X)/10))

for i in range(len(S)):
    S[i] = np.sqrt(((X[i+10][mid]-X[i][mid]))^2+((Y[i+10][mid]-Y[i][mid]))^2)
    
    
#S_min = the power law applies only to values greater than a minimum S[i] since
#few empirical phenomena obey the power law for all values of S[i]

#estimate the exponent alpha:
alpha_hat = 1 +n/(np.sum(np.ln(S)/S_min))

#the tail of the expected distribution obeys:
g = lambda x: ((alpha_hat-1)/S_min)*(x/S_min)^(-alpha_hat)

Levy_dist = g(S)

#Choosing S_min using the KS statistic

# maximize S_min in order to minimize the distance between the expected and
#actual distributions



