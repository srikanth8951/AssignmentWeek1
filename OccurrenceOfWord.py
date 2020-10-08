# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:28:44 2020

@author: hvsri
"""

def countOfWords(str1):
    str1 = str1 
    count = str1.count("USA")+str1.count("usa")
    return(count)

str1 = "Welcome to USA. usa awesome, isn't it?"
result = countOfWords(str1)
print("The USA count is: ",result)