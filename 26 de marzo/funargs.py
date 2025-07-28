# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:05:45 2021

@author: Juan Carlos
*arg

"""

def suma(*a):
    print("\n\tTipo de datos del argumento:",
         type(a))
    sum = 0
    for n in a:
        sum +=n
        #sum=sum+n

    print("Suma:",sum)
suma(1)
suma(5,8)
suma(1,6)
suma (2,8,10)
suma(0,1)
suma(1,2)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,5,6)
suma(1,2,3,5,6,7,8,9,10)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)
