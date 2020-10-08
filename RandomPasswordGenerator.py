# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 15:10:58 2020

@author: hvsri
"""

import random


def getRandomPassword():
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    number = int(input('Number of Passwords? - '))
    
    
    for i in range(number):
        password = ""
        for j in range(8):
            password += random.choice(chars)
        
        print("Random Password is ", password)
            
getRandomPassword()