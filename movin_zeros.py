# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:27:41 2022

@author: HP
"""

def move_zeros(lst):
    Zeros_lst=[a for a in lst if a!=0]
    NonZeros_lst=[b for b in lst if b==0]
    lst=Zeros_lst+NonZeros_lst
    
    
    return lst

print(move_zeros([1,0,3,0,7,7,5,0,3,4,0,2,4,5]))

def move_zeros2(array):
    return [x for x in array if x] + [0]*array.count(0)

print(move_zeros2([1,0,3,0,7,7,5,0,3,4,0,2,4,5]))