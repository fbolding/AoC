# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:07:28 2020

@author: freek
"""

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    for line in data:
        data[data.index(line)]= line.split('x')
    return data

dimensions=readAndFormatData('day2.txt')
req_paper=0
ribbon=0
for gift in dimensions:
    l=int(gift[0]); w=int(gift[1]); h=int(gift[2])
    slack=min([l*w,l*h,w*h])
    req_paper+=slack+2*l*w+2*l*h+2*w*h
    dim=[l,w,h]
    dim.sort()
    ribbon+=2*dim[0]+2*dim[1]+l*w*h
print(req_paper)
print(ribbon)