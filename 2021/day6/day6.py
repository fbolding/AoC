def readAndFormatData(filename):
    data= open(filename, 'r').read().split(',')
    data=[int(i) for i in data]
    return data
        
def FishSim_Brute(fish0,days):
    fish=fish0[:]
    for day in range(days):
        newfish=0
        i_fish=0
        while i_fish<len(fish):
            fish[i_fish]-=1
            if fish[i_fish]<0:
                newfish+=1
                fish[i_fish]=6
            i_fish+=1
        fish+=[8]*newfish
    return len(fish)

def FishSim_Eff(fish0,days):
    f_adult=[fish0.count(tleft) for tleft in range(7)]
    f_new=9*[0]
    for day in range(days):
        f_birth=f_adult[0]+f_new[0]
        for tleft in range(len(f_adult)):
            if tleft<6:
                f_adult[tleft]=f_adult[tleft+1]
            else:
                f_adult[tleft]=f_birth
        for tleft in range(len(f_new)):
            if tleft<8:
                f_new[tleft]=f_new[tleft+1]
            else:
                f_new[tleft]=f_birth
    return sum(f_adult)+sum(f_new)

def main():
    fish0=readAndFormatData('day6.txt')
    print(f'Part 1) {FishSim_Brute(fish0,80)}')
    print(f'Part 2) {FishSim_Eff(fish0,256)}')

main()