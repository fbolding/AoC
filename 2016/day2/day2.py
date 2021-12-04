def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    return data

directions={
    'R':1,
    'L':-1,
    'U':1j,
    'D':-1j
    } 
keypad1={
        '(-1+1j)':1,
        '(1j)':2,
        '(1+1j)':3,
        '(-1+0j)':4,
        '(0j)':5,
        '(1+0j)':6,
        '(-1-1j)':7,
        '(-1j)':8,
        '(1-1j)':9
        } 
keypad2={
     '(2j)':1,
     '(-1+1j)':2,
     '(1j)':3,
     '(1+1j)':4,
     '(-2+0j)':5,
     '(-1+0j)':6,
     '(0j)':7,
     '(1+0j)':8,
     '(2+0j)':9,
     '(-1-1j)':'A',
     '(-1j)':'B',
     '(1-1j)':'C',
     '(-2j)':'D'
     }  
   
def part1(data):
    code=[0]*len(data)
    i=0
    for line in data:
        pos=0j
        for ins in line:
            pos+=directions[ins]
            if abs(pos.real)>1 or abs(pos.imag)>1:
                pos-=directions[ins]
        code[i]=keypad1[str(pos)]
        i+=1
    return code

def part2(data):
    code=[0]*len(data)
    i=0
    for line in data:
        pos=0j
        for ins in line:
            pos+=directions[ins]
            if abs(pos.real)>2 or abs(pos.imag)>2 or abs(pos.real)+abs(pos.imag)>2:
                pos-=directions[ins]
        code[i]=keypad2[str(pos)]
        i+=1
    return code

def main():
    data=readAndFormatData('day2.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day2.txt')