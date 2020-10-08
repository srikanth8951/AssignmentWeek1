# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:10:30 2020

@author: hvsri
"""

from PIL import Image 
from numpy import* 
 
temp=Image.open('image.jpg') 
temp=temp.convert('1')      # Convert to black&white 
A = array(temp)             # Creates an array, white pixels==True and black pixels==False 
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A 
 
for i in range(len(A)): 
    for j in range(len(A[i])): 
        if A[i][j]==True: 
            new_A[i][j]=0 
        else: 
            new_A[i][j]=1 