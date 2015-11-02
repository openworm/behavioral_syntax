import behavioral_syntax as b_s

from behavioral_syntax.compression import time_warp as tw

def test_answer():
    assert tw.time_warp('1 2 3 4 5 5 2 3 3'.split(' ')) == ['1', '2', '3', '4', '5', '2', '3'
