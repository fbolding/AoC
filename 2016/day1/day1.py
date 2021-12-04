def readAndFormatData(filename):
    data= open(filename, 'r').read().split(', ')
    return data

def wrapdir(direction): #1=North, 2=East, 3=South, 4=West 
    if direction<1:
        direction=4
    elif direction>4:
        direction=1
    return direction
        
def part1(data):
    pos=[0,0]
    direction=1
    for move in data:
        steps=int(move[1:])
        if move[0]=='L':
            direction=wrapdir(direction-1)
        else:
            direction=wrapdir(direction+1)
        if direction==1:
            pos[1]+=steps
        elif direction==2:
            pos[0]+=steps
        elif direction==3:
            pos[1]-=steps
        elif direction==4:
            pos[0]-=steps
    return abs(pos[0])+abs(pos[1])

def part2(data):
    pos=[0,0]
    poslog=[]
    direction=1
    HQ=[0,0]
    for move in data:
        steps=int(move[1:])
        if move[0]=='L':
            direction=wrapdir(direction-1)
        else:
            direction=wrapdir(direction+1)
        if direction==1:
            for i in range(steps):
                pos[1]+=1
                if pos in poslog:
                    HQ=pos[:]
                poslog.append(pos[:])
        elif direction==2:
            for i in range(steps): 
                pos[0]+=1
                if pos in poslog:
                    HQ=pos[:]
                poslog.append(pos[:])
        elif direction==3:
            for i in range(steps):
                pos[1]-=1
                if pos in poslog:
                    HQ=pos[:]
                poslog.append(pos[:])
        elif direction==4:
            for i in range(steps):
                pos[0]-=1
                if pos in poslog:
                    HQ=pos[:]
                poslog.append(pos[:])
        if abs(HQ[0])+abs(HQ[1])!=0:
            break
    return abs(HQ[0])+abs(HQ[1])

def main():
    data=readAndFormatData('day1.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day1.txt')
#check=part2(['R8','R4','R4','R8'])
