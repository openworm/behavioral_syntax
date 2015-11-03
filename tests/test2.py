import numpy as np

from behavioral_syntax.compression import time_warp as tw
from behavioral_syntax.metrics import dynamic_time_warp as dtw

A = np.array([[ 0.7696172 ,  0.78793319,  0.28336053],
       [ 0.24157021,  0.79534655,  0.14525486],
       [ 0.86594475,  0.09850758,  0.78865837]])
       
B = np.array([[ 0.16536915,  0.593412  ,  0.71047034],
       [ 0.45331466,  0.49425367,  0.38858558],
       [ 0.80325654,  0.30417891,  0.81123514],
       [ 0.99096171,  0.25832039,  0.76569555]])

def test_answer():
    assert tw.time_warp('1 2 3 4 5 5 2 3 3'.split(' ')) == ['1', '2', '3', '4', '5', '2', '3']
    assert dtw.DTW(A,B) == 1.626742841248932
