# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:24:36 2020

@author: freek
"""

instructions= open('day3.txt', 'r').read()
Rpos=[0,0]
Spos=[0,0]
stringpos= str(Rpos)
stringhouses= [stringpos[:]]
robot=False
for ins in instructions:
    if robot==False:
        if ins=='^':
            Spos[1]+=1
        elif ins=='v':
            Spos[1]+=-1
        elif ins=='>':
            Spos[0]+=1
        elif ins=='<':
            Spos[0]+=-1
        stringpos=str(Spos)
        robot=True
        print(f'Spos={Spos}')
    elif robot==True:
        if ins=='^':
            Rpos[1]+=1
        elif ins=='v':
            Rpos[1]+=-1
        elif ins=='>':
            Rpos[0]+=1
        elif ins=='<':
            Rpos[0]+=-1
        stringpos=str(Rpos)
        robot=False
        print(f'Rpos={Rpos}')
    stringhouses.append(stringpos[:])
        
unique_houses=list(set(stringhouses))
print(f'Part 1) Unique houses encounterd is {len(unique_houses)}')
