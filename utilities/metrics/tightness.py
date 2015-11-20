from behavioral_syntax.utilities.angle_and_skel import angle2skel
import numpy as np
import numpy.linalg as la

def mid_body_angle(angle_vector):
    m_a = np.mean(angle_vector)
    N = len(angle_vector)
    X, Y = angle2skel(angle_vector,m_a,N,1)
    
    L = len(X)
    mid = int(L/2)
    
    v1 = np.array([(Y[L-1]-Y[mid])/(X[L-1]-X[mid]),1])
    v2 = np.array([(Y[mid]-Y[0])/(X[mid]-X[0]),1])
     
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)


	