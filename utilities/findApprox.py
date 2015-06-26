import numpy as np

def findApprox(traj, patternTraj, r2Thresh):
    
#Input
#   traj        - A length(trajectory) by number of trajectories matrix
#   patternTraj - A length(trajectory) by 1 vector
#   r2Thresh    - The threshold R^2 value for definining a match
# 
# Output
#   matchInds   - The indices of any matching trajectories

    N = np.shape(traj)[1]
    
    #initialise
    matchInds = np.zeros(N)
    
    
    # loop through trajectories in traj
    for i in range(N):
        # calculate the correlation between the current trajectory and the
        # pattern trajectory
        R = np.corrcoef([row[i] for row in Q], patternTraj);
        R2 = R[0][1]**2;
        
    
        if R2 >= r2Thresh and sign(R[0][1]) > 0:
            matchInds(i) = 1
    
    return matchInds
