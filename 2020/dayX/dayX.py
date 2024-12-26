# -*- coding: utf-8 -*-
"""

@author: freek
"""
def read_data(filename):
    data= open(filename, 'r').read().split('\n')
    for x in data:
        data[data.index(x)]=int(x)
    return data

def part1(data):
	return 0

def part2(data):
	return 0
 
def main():   
    data= read_data('input.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')
    
def timedMain():
    from timeit import default_timer as timer
    start=timer()
    main()
    end=timer()
    print(f'Elapsed time= {end-start} seconds')

timedMain()