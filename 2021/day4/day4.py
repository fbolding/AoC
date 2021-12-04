import numpy as np

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    nboards=int((len(data)-1)/6)
    boards=np.zeros((nboards,5,5))
    cur_board=-1
    i_line=0
    for line in data:
        if i_line==0:
            draw=line.split(',')
            draw=[int(i) for i in draw]
        else:
            if line=="":
                cur_board+=1
                cur_row=0
            else:
                row_num=[]
                for i in range(len(line)):
                    if (line[i]!=' ' and i==0) or (line[i]!=' ' and line[i-1]==' '):
                        if i<len(line)-1 and line[i+1]!=' ':
                            row_num.append(int(line[i]+line[i+1]))
                        else:
                            row_num.append(int(line[i]))
                boards[cur_board,cur_row,]=row_num
                cur_row+=1
        i_line+=1
    return draw,boards

def checkBingo(board):
    Bingo=False
    for i in range(5):
        if np.sum(board[i,:])==-5:
            Bingo=True
        if np.sum(board[:,i])==-5:
            Bingo=True
    return Bingo
        
def part1(draw,boards1):
    #boards1=boards[:]
    nboards=boards1.shape[0]
    correct_nums=[0]*nboards
    for num in draw:
        for b_i in range(nboards):
            board=boards1[b_i,:,:]
            if num in board:
               board=np.where(board==num,-1,board) 
               correct_nums[b_i]+=1
               if checkBingo(board):
                   return (np.sum(board)+correct_nums[b_i])*num
               else:
                   boards1[b_i,:,:]=board

def part2(draw,boards2):
    #boards2=boards[:]
    nboards=boards2.shape[0]
    won=[0]*nboards
    correct_nums=[0]*nboards
    for num in draw:
        for b_i in range(nboards):
            board=boards2[b_i,:,:]
            if num in board:
               board=np.where(board==num,-1,board) 
               correct_nums[b_i]+=1
               if checkBingo(board):
                   won[b_i]=1
                   if sum(won)==nboards:
                       sumb=np.sum(board)
                       checked=correct_nums[b_i]
                       return (sumb+checked)*num
               else:
                   boards2[b_i,:,:]=board

def main():
    draw,boards=readAndFormatData('day4.txt')
    print(f'Part 1) {part1(draw,boards)}')
    draw,boards=readAndFormatData('day4.txt') #Load data again since running part 1 overwrote the values
    print(f'Part 2) {part2(draw,boards)}')

main()
#draw,boards=readAndFormatData('day4_test.txt')