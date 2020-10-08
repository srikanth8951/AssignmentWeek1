# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def mixString():
    str1 = 'Abc'
    str2 = 'Xyz'
    
    strrev = str2[::-1]
    str3 = ''
    
    for i in range(len(str1)):
        str3 = str3+str1[i]
        str3 = str3+strrev[i]
        
    return str3
    
mix_String = mixString()

print(mix_String)


   