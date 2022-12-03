def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    res=[]
    for line in data:
        res.append([line[:len(line)//2],line[len(line)//2:]])
    return res
 
def calcPriority(char):
    intChar=ord(char)
    if intChar>96:
        prio=intChar-96
    else:
        prio=intChar-64+26
    return prio  

def compareCompartments(comp1,comp2):
    shared=''
    for item in comp1:
        if item in comp2 and item not in shared:
            shared+=item
    return shared

def part1(data):
    sumPrio=0
    for rucksack in data:
        shared=compareCompartments(rucksack[0],rucksack[1])
        for item in shared:
            sumPrio+=calcPriority(item)
    return sumPrio

def compareRucksacks(ruck1,ruck2,ruck3):
    for item in ruck1[0]+ruck1[1]:
        if item in ruck2[0]+ruck2[1] and item in ruck3[0]+ruck3[1]:
            return item

def part2(data):
    sumPrio=0
    for i in range(len(data)//3):
        ind=i*3
        badge=compareRucksacks(data[ind],data[ind+1],data[ind+2])
        sumPrio+=calcPriority(badge)
    return sumPrio

def main():
    data=readAndFormatData('day3.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day3.txt')