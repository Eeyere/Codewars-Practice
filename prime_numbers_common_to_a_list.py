# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:06:04 2022

@author: HP
"""
     
    
def sum_for_list(lst):
    c={}

    for a in lst:
        factors_a=set([factor for factor in range(2,abs(a)+1) if (a%factor ==0 and len([PF for PF in range(2,factor+1) if factor%PF==0])==1)])
        
        for d2 in sorted(list(factors_a)):
            if a%d2==0 and d2 in c:
                c[d2]+=a
            elif a%d2==0 and d2 not in c:
                c[d2]=a

    return ([[key,c[key]] for key in sorted(list(c.keys()))])
    

print(sum_for_list([-15, -21, -24, -30, -45]))

