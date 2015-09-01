# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 07:28:51 2015

@author: aidanrocke
"""

def time_warp(ts):
    #""" Return a new list in which all adjacent
       # duplicates from ts have been removed.
    #"""
    result = []
    most_recent_elem = None
    for e in ts:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


