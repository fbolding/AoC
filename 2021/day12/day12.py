def readAndFormatData(filename):
    data= open(filename, 'r').read().split('\n')
    data=[line.split('-') for line in data]
    return data

def getCaves(data):
    cavelist=set()
    for i in data:
        cavelist.add(i[0])
        cavelist.add(i[1])
    bigcaves=set()
    smallcaves=set()
    for cave in cavelist:
        if cave.isupper():
            bigcaves.add(cave)
        else:
            smallcaves.add(cave)    
    return cavelist, bigcaves, smallcaves

def getLinks(caves,data):
    links={}
    for cave in caves:
        link=set()
        for l in data:
            if l[0]==cave:
                link.add(l[1])
            elif l[1]==cave:
                link.add(l[0])
        links[cave]=link
    return links     

def dfs1(visited,links,loc):
   if loc=='end':
       return 1
   paths=0
   for pot_cave in links[loc]:
       if pot_cave.islower():
           if pot_cave not in visited:
               paths+=dfs1(visited|{pot_cave},links,pot_cave)
       else:
           paths+=dfs1(visited|{pot_cave},links,pot_cave)
   return paths

def dfs2(visited,visited_twice,links,loc):
   if loc=='end':
       return 1
   paths=0
   for pot_cave in links[loc]:
       if pot_cave.islower():
           if pot_cave not in visited:
               paths+=dfs2(visited|{pot_cave},visited_twice,links,pot_cave)
           elif pot_cave in visited and len(visited_twice)<1 and pot_cave!='start':
               paths+=dfs2(visited,visited_twice|{pot_cave},links,pot_cave) 
       else:
           paths+=dfs2(visited|{pot_cave},visited_twice,links,pot_cave)
   return paths

def part1(data):
    caves,bcaves,scaves=getCaves(data)
    links=getLinks(caves,data)
    npaths=dfs1({'start'},links,'start')
    return npaths

def part2(data):
    caves,bcaves,scaves=getCaves(data)
    links=getLinks(caves,data)
    npaths=dfs2({'start'},set(),links,'start')
    return npaths

def main():
    data=readAndFormatData('day12.txt')
    print(f'Part 1) {part1(data)}')
    print(f'Part 2) {part2(data)}')

main()
data=readAndFormatData('day12.txt')