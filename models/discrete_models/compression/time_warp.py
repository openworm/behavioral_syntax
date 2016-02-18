# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 07:28:51 2015

@author: aidanrocke
"""

from behavioral_syntax.utilities.string_conversion import plist_to_pstr

def time_warp(ts):
    """
    >>> time_warp('1 2 3 4 5 5 2 3 3'.split(' '))
    ['1', '2', '3', '4', '5', '2', '3']
    """
    
    ts = ts.split(' ')
    result = []
    most_recent_elem = None
    for e in ts:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result
    
def time_warp2(ts):
    """
    >>> time_warp2('1 2 3 4 5 5 5 2 3 3 3 3'.split(' '))
    '1 2 3 4 5 x3 2 3 x4'
    """
    
    ts = list(map(int,ts.split(' ')))
    
    result = []
    j = 1
    most_recent_elem = None
    for i in range(len(ts)):
        if ts[i] == most_recent_elem:
            j+=1
        else:
            result=result+[most_recent_elem,'x'+str(j)]
            most_recent_elem = ts[i]
            j = 1
            
    #result = plist_to_pstr([result])
            
    return result
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

def test_answer():
    assert time_warp('1 2 3 4 5 5 2 3 3'.split(' ')) == ['1', '2', '3', '4', '5', '2', '3']

