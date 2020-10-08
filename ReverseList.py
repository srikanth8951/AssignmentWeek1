# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:36:21 2020

@author: hvsri
"""

def reverselist(list1):
    list2 = []
    print("After Reversing list")
    for i in range(len(list1)-1, -1,-1):
        list2.append(list1[i])    
    print(list2)
    
    
list1 = [10, 20, 30, 40, 50]
print("List Before reversing", list1)

reverselist(list1)
