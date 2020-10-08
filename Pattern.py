# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:26:50 2020

@author: hvsri
"""

def pattern(number):
    
    for i in range(0,number):
        
        for j in range(0, i+1):
            print("*",end=" ")
            
        print()
     
    for k in range(number, 0, -1):
        
        for l in range(k, 0, -1):
            print("*", end=" ")
          
        print()


print("Enter the Number")
number = int(input())

pattern(number)