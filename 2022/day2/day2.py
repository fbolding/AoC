def readAndFormatData(filename):
    shapeDict={
        'X':1,
        'Y':2,    
        'Z':3,
        'A':1,
        'B':2,
        'C':3
        }
    data= open(filename, 'r').read().split('\n')
    result=[]
    for line in data:
        line=line.split(' ')
        result.append([*map(shapeDict.get,line)])
    return result

def calcScore(rnd):
    diff=rnd[1]-rnd[0]
    if diff==0:
        return rnd[1]+3
    elif diff==1 or diff==-2:
        return rnd[1]+6
    else:
        return rnd[1]
      
def part1(data):
    scores=list(map(calcScore,data))
    return sum(scores)

def determineShape(rnd):
    if rnd[1]==2:
        return rnd[0]
    elif rnd[1]==1:
        shape=rnd[0]-1
        if shape<1:
            shape=3
    else:
        shape=rnd[0]+1
        if shape>3:
            shape=1
    return shape    

def part2(data):
    shapes=list(map(determineShape,data))
    scores=[]
    for i in range(len(shapes)):
        scores.append(calcScore([data[i][0],shapes[i]]))
    return sum(scores)

def main():
    data=readAndFormatData('day2.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day2.txt')