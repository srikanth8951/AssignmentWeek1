# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:26:11 2020

@author: hvsri
"""

def multiplication(num):
    
    print("Given Number Multiplication Table is:\n")
    for i in range(1,10+1):
        mul = i*num
        print(mul)
        
print("Enter the Number")
num = int(input())

multiplication(num)