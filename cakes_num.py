# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:52:10 2022

@author: HP
"""

# Dictionaries representing objects were made to divide between recipes and what is available
# the results appended to a list and the minimum is returned 

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

#Other forms of the code is shown below

def cakes2(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
    
def cakes(recipe, available):

    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])