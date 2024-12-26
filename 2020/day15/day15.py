# -*- coding: utf-8 -*-
"""

@author: freek
"""
def read_data(filename):
    data= open(filename, 'r').read().split(',')
    for x in data:
        data[data.index(x)]=int(x)
    return data

def play_game(original, n_turns):
	turn = 1
	nums = {}
	new = False
	while (turn <= n_turns):
		if (turn <= len(original)):
			speak = original[turn-1]
			nums [speak] = turn
			
		elif speak in nums:
			last = nums[speak]
			nums[speak] = turn - 1
			speak = turn - 1 - last
		else:
			nums[speak] = turn -1
			speak = 0
		turn +=1
	return speak
			
			
	
def part1(data):
	return play_game(data, 2020)

def part2(data):
	return play_game(data, 30000000)
 
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