f = h5py.File('C:/Users/ltopuser/behavioral_syntax/utilities/data.mat')

l1 = f.get('worm')

l2 = l1.get('posture')

l3 = l2.get('skeleton')

X = l3.get('x')

Y = l3.get('y')

angleArray, meanAngles = angle(X,Y)

scipy.io.savemat('angles.mat', dict(x=angleArray))
