def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    return data
   
def binLst2Dec(lst):
    bina=''
    for bit in lst:
        bina+=str(bit)
    return int(bina,2)
    
def part1(data):
    mc=[]
    lc=[]
    for column in range(len(data[0])):
        count=0
        for row in range(len(data)):
            count+=int(data[row][column])
        if count>len(data)/2:
            mc.append(1)
            lc.append(0)
        else:
            mc.append(0)
            lc.append(1)
    gam=binLst2Dec(mc)
    eps=binLst2Dec(lc)
    return gam*eps

def bitCriteria(data,key):
    use=[True]*len(data)
    for column in range(len(data[0])):
        zeros=[]
        ones=[]
        for row in range(len(data)):
            if use[row]==True:
                ratingBin=data[row]
                if data[row][column]=='0':
                    zeros.append(row)
                else:
                    ones.append(row)
        if (len(ones)>=len(zeros) and key=='Oxy') or (len(zeros)>len(ones) and key=='CO2'):
            SetFalse(use,zeros)
        else:
            SetFalse(use,ones)
    rating=int(ratingBin,2)
    return rating

def SetFalse(use,indices):
    for i in indices:
        use[i]=False
    return use

def part2(data):  
    return bitCriteria(data,'Oxy')*bitCriteria(data,'CO2')

def main():
    data=readAndFormatData('day3_test.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()