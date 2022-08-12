# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:01:48 2022

@author: HP
"""

def is_prime(num):
    a=[]
    if num<=0 or num==1:
        a.append(num)
    else:
        for i in range(2,num):
            if num%i==0:
                a.append(i)

    if len(a)==0:
        return True
    else:
        return False
        
print(is_prime(73))