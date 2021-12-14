import collections

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n\n')
    polymer=data[0]
    rules=data[1].split('\n')
    rules=[line.split(' -> ') for line in rules]
    return polymer,rules
        
def part1(poltemp,rules,n):
    polymer=poltemp
    step=1
    while step<n+1:
        polynew=polymer
        lpbi=[0]*len(polymer) #Count how many Letters are Placed Before each Index in the original polymer, to correct later indices
        for i in rules:
            if i[0] in polymer:
                place=[]
                p_c1=[p for p,c in enumerate(polymer) if c==i[0][0]]
                if p_c1[-1]==len(polymer)-1:
                    p_c1.pop()
                for ii in p_c1:
                    if polymer[ii+1]==i[0][1]:
                        place.append(ii+1+lpbi[ii+1])
                        lpbi[ii+1:]=[x+1 for x in lpbi[ii+1:]]
                for ii in place:
                    polynew=polynew[:ii]+i[1]+polynew[ii:]
        polymer=polynew
        step+=1
    c=collections.Counter(polymer).most_common()
    return c[0][1]-c[-1][1]

def part2(poltemp,rules,n):
    answer2='No answer'
    return answer2

def main():
    pol,rules=readAndFormatData('day14.txt')
    print(f'Part 1) {part1(pol,rules,10)}')
    print(f'Part 2) {part2(pol,rules,40)}')

main()