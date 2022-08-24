# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:52:10 2022

@author: HP
"""
r={'flour': 500, 'sugar': 200, 'eggs': 1}
a={'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

def cakes(recipe, available):
    aa=[]
    for key in recipe:
        if key in available:
            aa.append(available[key]/recipe[key])
        else:
            aa.append(0)    
    
    return int(min(aa))

print(cakes(r,a))
