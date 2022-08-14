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

#Other shorter codes shown below:

def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
            
print(rgb2(67,255,-3))               
            
def rgb3(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
    
print(rgb3(67,255,-3))    


def rgb4(r, g, b):
    def get_hex(s):
        if s > 255: s = 255
        if s < 0: s = 0
        return hex(s)[2:].upper() if len(hex(s)[2:]) > 1 else "0" + hex(s)[2:]
    return get_hex(r) + get_hex(g) + get_hex(b)