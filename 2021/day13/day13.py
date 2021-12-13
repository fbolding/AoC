import numpy as np

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n\n')
    ins=[line.split(',') for line in data[0].split('\n')]
    folds=data[1].split('\n')
    return ins,folds

def createGrid(folds):
    for f in folds:
        f=f.split(' ')
        f_dir=f[2][0]
        f_line=int(f[2][2:])
        if f_dir=='y':
            ymax=f_line*2+1
        else:
            xmax=f_line*2+1
    grid=np.zeros([ymax,xmax])
    return grid

def placeDots(paper,ins):
    for i in ins:
        paper[int(i[1]),int(i[0])]=1
    return paper

def foldPaper(paper,folds):
    stop=False
    for f in folds:
        if len(f)==1: # To make sure it works with only one fold instruction as well
            f=folds
            stop=True
        f=f.split(' ')
        f_dir=f[2][0]
        f_line=int(f[2][2:])
        if f_dir=='y':
            p1=paper[:f_line,:]
            p2=paper[f_line+1:,:]
            p2=np.flip(p2,0)
        else:
            p1=paper[:,:f_line]
            p2=paper[:,f_line+1:]
            p2=np.flip(p2,1)
        paper=p1+p2
        if stop==True:
            break            
    return paper

def part1(ins,folds):
    paper=createGrid(folds[:2])
    paper=placeDots(paper,ins)
    paper=foldPaper(paper,folds[0])
    return int((paper!=0).sum())

def part2(ins,folds):
    paper=createGrid(folds[:2])
    paper=placeDots(paper,ins)
    paper=foldPaper(paper,folds)
    return paper

def main():
    ins,folds=readAndFormatData('day13.txt')
    print(f'Part 1) {part1(ins,folds)}')
    print(f'Part 2) \n{part2(ins,folds)}')

main()