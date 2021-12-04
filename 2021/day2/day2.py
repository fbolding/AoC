def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= line.split()
        
        i_line+=1
    return data
        
def part1(data):
    pos=[0,0]
    for line in data:
        if line[0]=='forward':
            pos[0]+=int(line[1])
        elif line[0]=='down':
            pos[1]+=int(line[1])
        elif line[0]=='up':
            pos[1]+=-int(line[1])
    return pos[0]*pos[1]

def part2(data):
    pos=[0,0]
    aim=0
    for line in data:
        if line[0]=='forward':
            pos[0]+=int(line[1])
            pos[1]+=int(line[1])*aim
        elif line[0]=='down':
            aim+=int(line[1])
        elif line[0]=='up':
            aim+=-int(line[1])
    return pos[0]*pos[1]

def main():
    data=readAndFormatData('day2.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day2.txt')