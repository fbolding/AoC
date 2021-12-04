# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:39:22 2020

@author: freek
"""

def readInput():
    inp= [int(x) for x in open('day2.txt', 'r').read().split(',')]
    return inp

def Interpreter(mem):
    inPoint=0
    opcode=0
    while opcode !=99:
        opcode=mem[inPoint]
        if opcode==1:
            inst=mem[inPoint:inPoint+4]
            mem[inst[3]]=mem[inst[1]]+mem[inst[2]]
            inPoint+=len(inst)
        elif opcode==2:
            inst=mem[inPoint:inPoint+4]
            mem[inst[3]]=mem[inst[1]]*mem[inst[2]]
            inPoint+=len(inst)
        elif opcode==99:
            inst=mem[inPoint]
    return mem
                       
def editCode(code,noun,verb):
    code[1]=noun
    code[2]=verb
    return code

def part1():
    Intcode=readInput()
    Intcode= editCode(Intcode,12,2)
    result=Interpreter(Intcode)
    print(f'Part 1) Value on position 0 is {result[0]}')

def part2():
    for noun in range(100):
        for verb in range(100):
            Intcode=readInput()
            Intcode=editCode(Intcode,noun,verb)
            result=Interpreter(Intcode)
            if result[0]==19690720:
                print(f'Part 2) Answer is {100*noun+verb}')
                break

def main():
    part1()
    part2()

main()
    
    



