# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:17:57 2020

@author: freek
"""
floor=0
position=0
basement=False
instructions= open('day1.txt', 'r').read()
for char in instructions:
    position+=1
    if char =='(':
        floor +=1
    elif char==')':
        floor +=-1
    if floor==-1 and basement==False:
        pos=position
        basement=True
print(floor)
print(pos)
    