def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    return data

def findLow(data):
    low_r=[]
    low_c=[]
    depth=[]
    for r in range(len(data)):
        for c in range(len(data[r])):
            p=int(data[r][c])
            neigh=[]
            if r!=0:
                neigh.append(data[r-1][c])
            if r!=len(data)-1:
                neigh.append(data[r+1][c])
            if c!=0:
                neigh.append(data[r][c-1])
            if c!=len(data[r])-1:
                neigh.append(data[r][c+1])
            neigh=[int(i) for i in neigh]
            if p<min(neigh):
                low_r.append(r)
                low_c.append(c)
                depth.append(p)
    return low_r,low_c,depth

def getBasinSize(grid,r,c):
    max_row=len(grid)-1
    max_col=len(grid[0])-1
    basin_cor=[[r,c]]
    i=0
    while i<len(basin_cor):
        rc=basin_cor[i][0]
        cc=basin_cor[i][1]
        d=int(grid[rc][cc])
        if rc!=0 and int(grid[rc-1][cc])!=9 and d<int(grid[rc-1][cc]) and [rc-1,cc] not in basin_cor:
            basin_cor.append([rc-1,cc])
        if rc!=max_row and int(grid[rc+1][cc])!=9 and d<int(grid[rc+1][cc]) and [rc+1,cc] not in basin_cor:
            basin_cor.append([rc+1,cc])
        if cc!=0 and int(grid[rc][cc-1])!=9 and d<int(grid[rc][cc-1]) and [rc,cc-1] not in basin_cor:
            basin_cor.append([rc,cc-1])
        if cc!=max_col and int(grid[rc][cc+1])!=9 and d<int(grid[rc][cc+1]) and [rc,cc+1] not in basin_cor:
            basin_cor.append([rc,cc+1])      
        i+=1
    return len(basin_cor)
       
def part1(data):
    [_,_,d]=findLow(data)
    return(sum(d)+len(d))

def part2(data):
    [rows,columns,_]=findLow(data)
    largest=[0]*3
    for basin in range(len(rows)):
        size=getBasinSize(data,rows[basin],columns[basin])
        if size>min(largest):
            largest[largest.index(min(largest))]=size
    return largest[0]*largest[1]*largest[2]

def main():
    data=readAndFormatData('day9.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()