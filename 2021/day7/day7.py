def readAndFormatData(filename):
    data= open(filename, 'r').read().split(',')
    data=[int(data[i]) for i in range(len(data))]
    return data
        
def part1(data):
    fuel=[0]*max(data)
    for dist in range(len(fuel)):
        fuel[dist]=sum([abs(data[crab]-dist) for crab in range(len(data))])
    return min(fuel)

def incrSum(val):
    return val*(val+1)/2
         
def part2(data):
    fuel=[0]*max(data)
    for dist in range(len(fuel)):
        fuel[dist]=sum([incrSum(abs(data[crab]-dist)) for crab in range(len(data))])
    return min(fuel)

def main():
    data=readAndFormatData('day7.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()