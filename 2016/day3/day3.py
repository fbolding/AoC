def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= line.split()
        data[i_line]=[int(i) for i in data[i_line]]
        i_line+=1
    return data

def CheckTriangle(triangle):
    sidecheck=0
    for ii,side in enumerate(triangle):
        if side<sum(triangle[:ii]+triangle[ii+1:]):
            sidecheck+=1
    if sidecheck<len(triangle):
        return 0
    else:
        return 1
            
def part1(data):
    valid=[0]*len(data)
    i=0
    for triangle in data:
        valid[i]=CheckTriangle(triangle)
        i+=1
    return sum(valid)

def part2(data):
    new_triangles=[]
    tri=[]
    for column in range(len(data[0])):
        for row in range(len(data)):
            tri.append(data[row][column])
            if len(tri)==3:
                new_triangles.append(tri[:])
                tri=[]
    return part1(new_triangles)

def main():
    data=readAndFormatData('day3.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day3.txt')