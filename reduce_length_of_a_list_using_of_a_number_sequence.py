# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:20:16 2022

@author: HP
"""
aaa=[-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
def solution(args):
    x=0;a=[];soln=[]
    while x<len(args):
        y=x
        if len(args[y:])>=3 and (args[y+1]-args[y]==1) and (args[y+2]-args[y+1]==1):
            a+=[args[y], args[y+1], args[y+2]]
            x+=3
            
        elif len(args[y:])>=2 and (args[y+1]-args[y]==1):
            a+=[args[y], args[y+1]]
            x+=2
            
        else:
            a+=[args[y]]
            x+=1

            
        if x <(len(args)) and args[x]-args[x-1]==1:
            y=x
        else:
            if len(a)>=3:
                soln.append(str(min(a))+'-'+str(max(a)))
                a=[]

            elif len(a)==2:
                soln.append(str(a[0]))
                soln.append(str(a[1]))
                a=[]

            else:
                soln.append(str(a[0]))
                a=[]
                
    return ','.join(soln)


print(solution(aaa))
                