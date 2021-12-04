# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:17:50 2020

@author: freek
"""

modules =[int(x) for x in open('day1.txt', 'r').read().split('\n')] #'r' specifies python the file is for reading. read actually reads the file object. split makes sure it splits on every next line
fuel_req=[0]*len(modules)

def fuelCalc(mass):
    fuel=mass//3-2
    if fuel>0:
        fuel+=fuelCalc(fuel)
    else:
        fuel=0
    return fuel
 
for module in modules:
    fuel_req[modules.index(module)]=fuelCalc(module)
    
print(f'Sum of fuel requirements is {sum(fuel_req)}')