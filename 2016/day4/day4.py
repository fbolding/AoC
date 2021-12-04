from collections import Counter

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    i_line=0
    for line in data:
        data[i_line]= line.replace('[','-').replace(']','').split('-')
        i_line+=1
    return data
        
def part1_old(data):
    answer1=0
    for room in data:
        keyword=room[-1]
        encrypt="".join(room[:-2])
        valid=True
        for i in range(1,len(keyword)):
            letter=keyword[i]
            prev_letter=keyword[i-1]
            occ=encrypt.count(letter)
            prev_occ=encrypt.count(prev_letter)
            if occ>prev_occ:
                valid=False
            elif occ==prev_occ and sorted([prev_letter,letter])!=[prev_letter,letter]:
                valid=False
        if valid==True:
            answer1+=int(room[-2])
    return answer1

def CheckRoom(room):
    mc=""
    encrypt="".join(room[:-2])
    occ_count=Counter(encrypt)
    true_occ_count=sorted(occ_count.items(), key=lambda x: (-x[1], x[0]))
    for ltr in true_occ_count[:5]:
        mc+=ltr[0]
    if mc==room[-1]:
        return True
    else:    
        return False

alphabet='abcdefghijklmnopqrstuvwxyz'
def Decrypt(room,secID):
    realname=[]
    for word in room[:-2]:
        realword=""
        for ltr in word:
            old_i=alphabet.index(ltr)
            new_i=((old_i+secID)%26)
            realword+=alphabet[new_i]
        realname.append(realword)
    return realname
    
def part1(data):
    answer1=0
    for room in data:
        if CheckRoom(room)==True:
            answer1+=int(room[-2])
    return answer1

def part2(data):
    sentence_log=[]
    for room in data:
        ID=int(room[-2])
        sentence=Decrypt(room,ID)
        if 'north' in sentence[0]:
            answer2=ID
        sentence_log.append(sentence)
    return answer2

def main():
    data=readAndFormatData('day4.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
#data=readAndFormatData('day4.txt')
# line='qzmt-zixmtkozy-ivhz-343[abcde]'
# room=line.replace('[','-').replace(']','').split('-')
# test=Decrypt(room,int(room[-2]))