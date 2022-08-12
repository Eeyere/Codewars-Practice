# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 08:52:46 2022

@author: HP
"""
#This fike conatins a function that can determine the word with the max count
# in a sentence 
#shown as a string
def high(x):
    # Code here
    x=x.split()
    letters =' abcdefghijklmnopqrstuvwxyz' 
    word_value=[]
    for index, word in enumerate(x):
        word_value.append(sum([letters.index(i) for i in word.lower()]))
        #print(word_value)
        
    return x[word_value.index(max(word_value))]

a=("the first trial")

print(high(a))
            
# Further practice 
bb='This is a trial of our practice code obtained with much zeal'
print("the highest word on the sentence {} is: {}".format(bb, high(bb)) )

bb="This is another word to try"
print ("the highest word on the sentence {} is: {}".format(bb, high(bb)) )