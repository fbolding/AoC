def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= int(data[i_line])
        i_line+=1
    return data
        
def part1(data):
    for idx, val in enumerate(data):
        if idx==0: 
            increase=0
        elif val>data[idx-1]:
            increase+=1
    return increase

def part2(data):
    answer2=0
    window=data[0:3]
    window.reverse()
    sumprev=sum(window)
    for i in range(3,len(data)):
        window.insert(0,data[i])
        window.pop()
        sumcur=sum(window)
        if sumcur>sumprev:
            answer2+=1
        sumprev=sumcur
    return answer2

def main():
    data=readAndFormatData('day1.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()