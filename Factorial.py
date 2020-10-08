# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:00:20 2020

@author: hvsri
"""
def factorial(number):
    num = number
    i = num-1
    while(i>0): 
        num = num*i
        i=i-1
        
        
    print("Factorial for a number", number,"is:", num)
    
    

print("Enter the Number")
number = int(input())
factorial(number)