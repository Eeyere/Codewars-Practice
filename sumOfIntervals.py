# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:24:13 2022

@author: HP
"""


def sum_of_intervals(intervals):

    k=len(intervals)
   
    while k!=0:
        new_list=intervals
        i=intervals[0]
        pop_items=[]
        append_items=[]
        for j in intervals:
            if j[0] in list(range(i[0],i[1]+1)):
                pop_items.append(intervals.index(j))
                append_items+=j
        
        intervals.append([min(append_items),max(append_items)])

        pop_items_sort=sorted(pop_items, reverse=True)        
        for ind,val in enumerate(pop_items_sort):
            intervals.pop(val)
                
        k-=1
    
    return sum([aaa[1]-aaa[0] for aaa in new_list])

