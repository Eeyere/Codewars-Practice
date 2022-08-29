# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:18:47 2022

@author: HP
"""

#n=60
aa =[]

def fibonacci(n):
    
    for i in range(n+1):
        if i in [0,1]:
            aa.append(i)
            print('first case ', aa, ' ', i, 'term')
        else:
            nn=aa[-i+1:]
            print(nn)
            for  j in range(i):
                if (j==0):
                    aa.append(1)
                    print('second case ',aa, ' ', j+1, ' of ', i, ' term')
                elif j==i-1:
                    aa.append(1)
                    print('last case ',aa, ' ', j+1, ' of ', i, ' term')
                else:
                    aa.append(nn[j-1]+nn[j])
                    print('third case ',aa, ' ', j+1, ' of ', i, ' term')
    return sum(aa[-i+1:])

print(fibonacci(50))
#print(fibonacci(2))
#print(fibonacci(3))
"""
(fibonacci(70), 190392490709135)
(fibonacci(60), 1548008755920)
(fibonacci(50), 12586269025)"""