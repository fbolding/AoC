# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:53:50 2020

@author: freek
"""
import pandas as pd

def readData():
    return pd.read_csv('day2.txt', header=None)[0].tolist()
    
def separateList(data):
    upperbound= [0]*len(data); lowerbound= [0]*len(data); letter= [0]*len(data); password= [0]*len(data) #Initializing lists
    for i in range(len(data)):
        line= data[i].replace('-',' ').replace(':','') #Replace hyphen and colon with whitespace
        sep_line=line.split()  #Splits string on every whitespace
        lowerbound[i]=int(sep_line[0]); upperbound[i]=int(sep_line[1]); letter[i]= sep_line[2]; password[i]= sep_line[3]        
    return lowerbound, upperbound, letter, password

def checkPasswords1(lowerbound,upperbound,letter,password):
    counter=0
    for i in range(len(password)):
        lettercount= password[i].count(letter[i])
        if lettercount>=lowerbound[i] and lettercount<=upperbound[i]:
            counter= counter+1           
    return counter

def checkPasswords2(pos1,pos2,letter,password):     
    counter=0
    for i in range(len(password)):
        occ=0
        if password[i][pos1[i]-1]==letter[i]:
            occ=occ+1
        if password[i][pos2[i]-1]==letter[i]:
            occ=occ+1
        if occ==1:
            counter=counter+1          
    return counter
    
def main():
    inputList=readData()
    low, up, let, pw= separateList(inputList)
    Nvalid_pw1= checkPasswords1(low,up,let,pw) #Part 1
    print('Part 1) ' + str(Nvalid_pw1) + ' passwords correct')
    Nvalid_pw2= checkPasswords2(low,up,let,pw) #Part 2
    print('Part 2) ' + str(Nvalid_pw2) + ' passwords correct')

main()