# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 07:28:51 2015

@author: aidanrocke
"""

def time_warp(ts):
    """
    >>> time_warp('1 2 3 4 5 5 2 3 3'.split(' '))
    '1', '2', '3', '4', '5', '2', '3']
    """
    result = []
    most_recent_elem = None
    for e in ts:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

def test_answer():
    assert time_warp('1 2 3 4 5 5 2 3 3'.split(' ')) == 5

