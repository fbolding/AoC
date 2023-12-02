import math

def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    data=[line.split(':') for line in data] # Remove Game X:
    data=[line[1].split(';') for line in data] # Split data in sets
    res = []
    for game in data:
        res2 = []
        for set in game:
            set = set.replace(',','')
            res3 = set.split(' ')
            res2.append(res3[1:])
        res.append(res2)
    return res

def part1(data):
    sum = 0
    cube_dict = {'red':12, 'green':13, 'blue':14}
    for game_idx, game in enumerate(data):
        valid = True
        for set in game:
            for idx in range(0,len(set),2):
                num = int(set[idx])
                color = set[idx+1]
                if num > cube_dict[color]:
                    valid = False
        if valid:
            sum += game_idx+1 # Game ID is one greater than game index
    return sum

def part2(data):      
    sum = 0
    for game_idx, game in enumerate(data):
        cube_dict = {'red':0, 'green':0, 'blue':0}
        for set in game:
            for idx in range(0,len(set),2):
                num = int(set[idx])
                color = set[idx+1]
                if num > cube_dict[color]:
                    cube_dict[color] = num
        power = math.prod(cube_dict.values())
        sum += power
    return sum

if __name__ == "__main__":
    data=readAndFormatData('day2.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')