def checknext(lastchange,current):
    if current == "|":
        if lastchange[0] == 1:
            return 0
        return 1
    elif current == "-":
        if lastchange[1] == 1:
            return 2
        return 3
    elif current == "L":
        if lastchange[0] == 1:
            return 2
        return 1
    
    elif current == "J":
        if lastchange[1] == 1:
            return 1
        return 3
    elif current == "7":
        if lastchange[1] == 1:
            return 0
        return 3
    elif current == "F":
        if lastchange[0] == -1:
            return 2
        return 0
        
def part2():
    file = open('input.txt','r')
    map = [row.replace("\n","") for row in file]
    moves = []
    cords = [[1,0,["|","L","J"]],[-1,0,["|","F","7"]],[0,1,["-","7","J"]],[0,-1,["-","F","L"]]]
    nextCord = -1
    counter = 0
    for i, row in enumerate(map):
        if "S" in row:
            moves.append([i,row.find("S")])

    for cord in cords:
        if map[moves[-1][0]+cord[0]][moves[-1][1]+cord[1]] in cord[2]:
            print(map[moves[-1][0]+cord[0]][moves[-1][1]+cord[1]])
            moves.append([moves[-1][0]+cord[0],moves[-1][1]+cord[1]])
            nextCord = checknext(cord,map[moves[-1][0]][moves[-1][1]])
            counter += 1
            break

    while map[moves[-1][0]][moves[-1][1]] != "S":
        moves.append([moves[-1][0]+cords[nextCord][0],moves[-1][1]+cords[nextCord][1]])
        nextCord = checknext(cords[nextCord],map[moves[-1][0]][moves[-1][1]])
        counter += 1

    print(moves)
    print(counter/2)

part2()