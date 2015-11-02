import behavioral_syntax as b_s

from b_s import compression.time_warp as tw

def test_answer():
    assert tw('1 2 3 4 5 5 2 3 3'.split(' ')) == ['1', '2', '3', '4', '5', '2', '3'
