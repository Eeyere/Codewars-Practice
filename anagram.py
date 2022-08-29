# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:43:58 2022

@author: HP
"""

cc=('abba', ['aabb', 'abcd', 'bbaa', 'dada'])



def anagrams(word, words):
    letters =' abcdefghijklmnopqrstuvwxyz'
    word_num=sorted([letters.find(w) for w in word])
    ans=[]
    for word_check in words:
        if sorted([letters.find(w2) for w2 in word_check])==word_num:
            ans.append(word_check)
        
    return ans


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))