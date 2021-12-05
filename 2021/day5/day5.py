import numpy as np

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= line.replace(',',' -> ').split(' -> ')
        data[i_line]=[int(i) for i in data[i_line]]
        i_line+=1
    return data

def sign(x):
    if x<0:
        return -1
    else:
        return 1

def createGrid(data):
    maxVal=0
    for line in data:
        if max(line)>maxVal:
            maxVal=max(line)
    grid= np.zeros((maxVal+1,maxVal+1))
    return grid

def createLine(endcor,diag):
    coords=[]
    if endcor[0]==endcor[2]: #x is equal
        nstep=(endcor[3]-endcor[1])
        for i in range(abs(nstep)+1):
            coords.append([endcor[0],endcor[1]+i*sign(nstep)])
    elif endcor[1]==endcor[3]: #y is equal
        nstep=(endcor[2]-endcor[0])
        for i in range(abs(nstep)+1):
            coords.append([endcor[0]+i*sign(nstep),endcor[1]])
    elif diag==True and abs(endcor[3]-endcor[1])==abs(endcor[2]-endcor[0]):       
        nstep=(endcor[2]-endcor[0])
        xdir=sign(endcor[2]-endcor[0])
        ydir=sign(endcor[3]-endcor[1])
        for i in range(abs(nstep)+1):
            coords.append([endcor[0]+i*xdir,endcor[1]+i*ydir])
    return coords

def mapClouds(data,diag):
    grid=createGrid(data)
    for line in data:
        coords=createLine(line,diag)
        for c in coords:
            grid[c[1]][c[0]]+=1
    return (grid>=2).sum()

def main():
    data=readAndFormatData('day5.txt')
    print(f'Part 1) {mapClouds(data,False)}')
    print(f'Part 2) {mapClouds(data,True)}')

main()