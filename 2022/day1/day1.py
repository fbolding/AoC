def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n\n')
    data=[list(map(int,line.split('\n'))) for line in data]
    return data
  
def sumAndSort(data):
    sumdata=[sum(elves) for elves in data]
    sumdata.sort(reverse=True)
    return sumdata
      
def part1(data):
    return data[0]

def part2(data):
    return data[0]+data[1]+data[2]

def main():
    data=readAndFormatData('day1.txt')
    sumdata=sumAndSort(data)    
    print(f'Part 1) {part1(sumdata)}')
    print(f'Part 2) {part2(sumdata)}')

main()