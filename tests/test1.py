import behavioral_syntax as b_s

from b_s import time_warp as tw
    
def test_answer():
    assert time_warp('1 2 3 4 5 5 2 3 3'.split(' ')) == 5
