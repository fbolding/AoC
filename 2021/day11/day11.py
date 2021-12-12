def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    data=[[int(i) for i in line] for line in data]
    return data

def getNeigh(r,c):
    neigh=[]
    if r!=0:
        neigh.append([r-1,c])
        if c!=0:
            neigh.append([r-1,c-1])
        if c!=9:
            neigh.append([r-1,c+1])
    if r!=9:
        neigh.append([r+1,c])
        if c!=0:
            neigh.append([r+1,c-1])
        if c!=9:
            neigh.append([r+1,c+1])
    if c!=0:
        neigh.append([r,c-1])
    if c!=9:
        neigh.append([r,c+1])
    return neigh

def part1(data):
    grid=data[:]
    nsteps=100
    flashes=0
    for i in range(nsteps):
        print('step) ',i)
        flashed=[]
        for r in range(len(grid)):
            for c in range(len(grid)):
                grid[r][c]+=1
                if grid[r][c]==10:
                    flashes+=1
                    grid[r][c]=0
                    flashed.append([r,c])
        ii=0
        while ii < len(flashed):
            neigh=getNeigh(flashed[ii][0],flashed[ii][1])
            for n in range(len(neigh)):
                if grid[neigh[n][0]][neigh[n][1]]!=0:
                    grid[neigh[n][0]][neigh[n][1]]+=1
                    if grid[neigh[n][0]][neigh[n][1]]==10:
                        flashes+=1
                        grid[neigh[n][0]][neigh[n][1]]=0
                        flashed.append([neigh[n][0],neigh[n][1]])
            ii+=1
    return flashes

def part2(data):
    grid=data[:]
    flashes=0
    step=0
    flashed=[]
    while len(flashed)<100:
        step+=1
        if step==94:
            print('here')
        flashed=[]
        for r in range(len(grid)):
            for c in range(len(grid)):
                grid[r][c]+=1
                if grid[r][c]==10:
                    flashes+=1
                    grid[r][c]=0
                    flashed.append([r,c])
        ii=0
        while ii < len(flashed):
            neigh=getNeigh(flashed[ii][0],flashed[ii][1])
            for n in range(len(neigh)):
                if grid[neigh[n][0]][neigh[n][1]]!=0:
                    grid[neigh[n][0]][neigh[n][1]]+=1
                    if grid[neigh[n][0]][neigh[n][1]]==10:
                        flashes+=1
                        grid[neigh[n][0]][neigh[n][1]]=0
                        flashed.append([neigh[n][0],neigh[n][1]])
            ii+=1
    return step+100

def main():
    data=readAndFormatData('day11.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day11.txt')