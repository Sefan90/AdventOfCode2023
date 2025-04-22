def part1():
    file = open('input.txt','r')
    map = []
    map90 = []
    i = 0
    map.append([])
    map90.append([])
    for row in file:
        if row == "\n":
            i += 1
            map.append([])
            map90.append([])
        else:
            map[i].append(row.replace("\n",""))
            for x, c in enumerate(row.replace("\n","")):
                if len(map90[i]) <= x:
                    map90[i].append([])
                map90[i][x].append(c)

    for i, pattern in enumerate(map):
        for j, row in enumerate(pattern):
            if j+1 < len(map[i]):
                test = True
                for x in range(len(row)):
                    if row[x] != map[i][j+1][x]:
                        test = False
                        break
                if test == True:
                    print("Yeye")


    print(map)
    print(map90[0])
    

part1()