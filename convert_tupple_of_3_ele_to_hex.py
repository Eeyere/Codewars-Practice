# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:31:27 2022

@author: HP
"""
# A code that retruns hexadecimal values

def rgb(r, g, b):
    a=(r,g,b)
    rgb_array=list(a)
    rgb_hex= [0]*3
    rgb_str =""

    for ind,val in enumerate(rgb_array):
        if val>255:
            rgb_hex[ind]=hex(255)[2:]
        elif val<0:
            rgb_hex[ind]=hex(0)[2:]
        else:
            rgb_hex[ind]=hex(val)[2:]
            
    for i in rgb_hex:
        if len(i)==1:
            rgb_str+="0"+i
        else:
            rgb_str+=i
            
    return rgb_str.upper()


print(rgb(67,255,-3))        
            
            
            
    
    