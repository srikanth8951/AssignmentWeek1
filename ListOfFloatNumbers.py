# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:03:38 2020

@author: hvsri
"""

l = []
i=0

while(i<5):
    
    print("Enter the float number")
    num = float(input())
    
    l.insert(i,num)
    i=i+1
    
print(l)

