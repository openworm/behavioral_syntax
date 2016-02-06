# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:47:37 2016

@author: aidanrocke
"""

def pstr_to_plist(pos_string):
    N = len(pos_string)
    
    sequences = []
    
    for i in range(N):
        alpha1 = pos_string[i].split(' ')
        alpha2 = list(map(int,[i for i in alpha1 if i != '']))
        sequences.append(alpha2)
        
    return sequences
    
def plist_to_pstr(pos_list):
    N = len(pos_list)
    
    strings = []
    
    for i in range(N):
        alpha = list(map(str,pos_list[i]))
        alpha2 = ' '.join(alpha)
        strings.append(alpha2)
        
    return strings