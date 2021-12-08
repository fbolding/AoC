def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    inp=[]
    out=[]
    for line in data:
        [inp_i,out_i]=line.split(' | ')
        inp.append(inp_i.split(' '))
        out.append(out_i.split(' '))
    return inp,out
        
def part1(data):
    occ=0
    for line in data:
        for digit in line:
            nseg=len(digit)
            if nseg==2 or nseg==4 or nseg==3 or nseg==7:
                occ+=1
    return occ

seg2dig={
    'abcefg':0,
    'cf':1,
    'acdeg':2,
    'acdfg':3,
    'bcdf':4,
    'abdfg':5,
    'abdefg':6,
    'acf':7,
    'abcdefg':8,
    'abcdfg':9}

def alphSort(string):
    s=''.join(sorted(string))
    return s

def decode(inp):
    lengths=[len(i) for i in inp]
    one=inp[lengths.index(2)]
    seven=inp[lengths.index(3)]
    four=inp[lengths.index(4)]
    eight=inp[lengths.index(7)]
    a=seven.replace(one[0],'').replace(one[1],'')
    len5=[inp[ii] for ii in [i for i,e in enumerate(lengths) if e==5]]
    for len5dig in len5:
        if one[0] in len5dig and one[1] in len5dig:
            three=len5dig
    len6=[inp[ii] for ii in [i for i,e in enumerate(lengths) if e==6]]
    for len6dig in len6:
        if three[0] in len6dig and three[1] in len6dig and three[2] in len6dig and three[3] in len6dig and three[4] in len6dig:
            nine=len6dig
    e=eight.replace(nine[0],'').replace(nine[1],'').replace(nine[2],'').replace(nine[3],'').replace(nine[4],'').replace(nine[5],'')
    b=nine.replace(three[0],'').replace(three[1],'').replace(three[2],'').replace(three[3],'').replace(three[4],'')
    for len5dig in len5:
        if e in len5dig:
            two=len5dig
    for len5dig in len5:
        if len5dig !=two and len5dig!=three:
            five=len5dig
    c=one.replace(five[0],'').replace(five[1],'').replace(five[2],'').replace(five[3],'').replace(five[4],'')
    sixdiff=eight.replace(c,'')
    for len6dig in len6:
        if len6dig!=nine and alphSort(len6dig)==alphSort(sixdiff):
            six=len6dig
        elif len6dig!=nine:
            zero=len6dig
    d=eight.replace(zero[0],'').replace(zero[1],'').replace(zero[2],'').replace(zero[3],'').replace(zero[4],'').replace(zero[5],'')
    f=one.replace(c,'')
    g=two.replace(a,'').replace(c,'').replace(d,'').replace(e,'')
    decdict={
        a:'a',
        b:'b',
        c:'c',
        d:'d',
        e:'e',
        f:'f',
        g:'g'}   
    return decdict

def decode_dig(dig,decdict):
    decoded=''
    for ltr in dig:
        decoded+=decdict[ltr]
    return decoded

def part2(inp,out):
    sumout=0
    for i in range(len(inp)):
        decdict=decode(inp[i])
        for ii,dig in enumerate(out[i]):
            dig_dec=decode_dig(dig,decdict)
            sumout+=seg2dig[alphSort(dig_dec)]*pow(10,3-ii)
    return sumout

def main():
    inp,out=readAndFormatData('day8.txt')
    print(f'Part 1) {part1(out)}')
    print(f'Part 2) {part2(inp,out)}')

main()