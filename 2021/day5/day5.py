def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= line
        i_line+=1
    return data
        
def part1(data):
    answer1='1'
    return answer1

def part2(data):
    answer2=2
    return answer2

def main():
    data=readAndFormatData('dayX.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

#main()
data=readAndFormatData('dayX.txt')