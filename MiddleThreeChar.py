# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:55:42 2020

@author: hvsri
"""

def middleWord(str1, str2):
    middleNumber1 = int(len(str1)/2)    
    middelString1 = str1[middleNumber1-1 : middleNumber1+2]
    
    middleNumber2 = int(len(str2)/2)    
    middleString2 = str2[middleNumber2-1 : middleNumber2+2]
    
    return middelString1, middleString2

str1 = "JhonDipPeta"
str2 = "JaSonAy"
    
print(middleWord(str1, str2))




