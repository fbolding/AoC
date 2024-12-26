# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:31:05 2020

@author: freek
"""

def readData():
    return open('day3.txt', 'r').read().split('\n')

def readSjors():
    return open('data3.txt', 'r').read().split('\n')

def collisionCounter(forest,stepCol,stepRow):
    collisions=0
    width=len(forest[0])
    Nrows=round(len(forest)/stepRow)
    for i in range(Nrows):
        row= stepRow*i    
        col= stepCol*i
        while col>width-1:
            col+=-width
        if forest[row][col]=='#':
            collisions+=1
    return collisions
        
def main():
    forest=readData()
    slope_2= collisionCounter(forest,3,1)
    print('Part 1) '+ str(slope_2) + ' trees encountered')
    multiply= slope_2*collisionCounter(forest,1,1)*collisionCounter(forest,5,1)*collisionCounter(forest,7,1)#*collisionCounter(forest,1,2)
    print('Part 2) '+ str(multiply))

def timedMain():
    from timeit import default_timer as timer
    start=timer()
    main()
    end=timer()
    print(f'Elapsed time= {end-start} seconds')

timedMain()