# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:46:13 2022

@author: HP
"""

a=([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])


def valid_solution(board):
    ans=True
    import numpy as np
    b=np.array(board)
    c=np.transpose(a)
    
    if np.max(b)>9 or np.min(b)<1:
        ans=False
    
    for aa in [0,3,6]:
            for bb in [0,3,6]:
                b_3=b[aa:aa+3,bb:bb+3]
            if np.sum(b_3)!=45:
                ans= False               
    
    for ii in c:
        if np.sum(ii) !=45:
            ans= False
                   
    return ans
   
def valid_solution2(a):
    try:
        c=[[a[x][i]for x in range(9)if a[x][i] in range(1,10)]for i in range(9)]
        e=[i for i in a]
        f=[[a[x+n][i+m]for i in range(3)for x in range(3)]for m in range(0,9,3)for n in range(0,9,3)]
        return all([len(set(i))==9for i in c+e+f])
    except:
        return False


print(valid_solution(a))

print(valid_solution2(a))