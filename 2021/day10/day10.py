def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    return data
     
pairs={')':'(',']':'[','}':'{','>':'<'}
openers='([{<'
closers=')]}>'

def part1(data):
    score=0
    incomp=[]
    score_table={')':3,']':57,'}':1197,'>':25137}
    for line in data:
        open_chunk=[]
        for char in line:
            if char in openers:
                open_chunk.append(char)
            else:
                if pairs[char]==open_chunk[-1]:
                    open_chunk.pop()
                else:
                    score+=score_table[char]
                    incomp.append(data.index(line))
                    break
    return score,incomp

def part2(data,incomp):
    pairs_inv={v:k for k,v in pairs.items()}
    i=-1
    score_table={')':1,']':2,'}':3,'>':4}
    all_scores=[]
    for line in data:
        i+=1
        if i not in incomp:
            open_chunk=[]
            for ii,char in enumerate(line):
                if char in openers:
                    open_chunk.append(char)
                elif pairs[char]==open_chunk[-1]:
                    open_chunk.pop()    
                if ii==len(line)-1:
                    completion=[pairs_inv[c] for c in open_chunk]
                    completion.reverse()
                    score=0
                    for c in completion:
                        score=score*5+score_table[c]
                    all_scores.append(score)
    all_scores.sort()
    return all_scores[int(len(all_scores)/2-0.5)]

def main():
    data=readAndFormatData('day10.txt')
    [score1,incomp]=part1(data)
    print(f'Part 1) {score1}')
    print(f'Part 2) {part2(data,incomp)}')

main()