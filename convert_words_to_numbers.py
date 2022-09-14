# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:22:09 2022

@author: HP
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:04:00 2022

@author: HP
"""

numb= 'one-million two hundred thousand five hundred and forty-six'
num2='eight hundred million, eight hundred and eighty eight thousand, eight hundred and eighty eight'

def parse_int(string):
    import numpy as np
    splitted_string=string.replace('-',' ').replace(',',' ').split(' ')
    num_value=0
    numbers={'':0,'and':0,'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'forteen':14,'fifteen':15,'sisteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20, 'thirty':30,'fourty':40,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
    numbers_clas={'million':0,'thousand':0,'hundred':0,'tens':0,'units':0}
    number_clas={'million':0,'thousand':0,'hundred':0,'tens':0,'units':0}
    for num in splitted_string:
        print(num)

        if num == 'million':
            val=number_clas['thousand']+number_clas['hundred']+num_value  
            numbers_clas[num]=val*1000000
            numbers_clas['thousand']=0
            numbers_clas['hundred']=0
            num_value=0
            number_clas={'million':0,'thousand':0,'hundred':0,'tens':0,'units':0}

        elif num == 'thousand':
            val=number_clas['hundred']+num_value  
            numbers_clas[num]=val*1000
            numbers_clas['hundred']=0
            num_value=0
            number_clas={'million':0,'thousand':num_value*1000,'hundred':0,'tens':0,'units':0}

        elif num=='hundred':
            numbers_clas[num]=num_value*100
            number_clas={'million':0,'thousand':0,'hundred':num_value*100,'tens':0,'units':0}
            num_value=0
        else:
            num_value += numbers[num]
        
    val=numbers_clas['million']+numbers_clas['thousand']+numbers_clas['hundred']+num_value         
    return (val)

print(parse_int(num2))