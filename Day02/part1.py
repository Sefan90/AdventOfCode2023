def countCubes(set):
    for cubes in set.split(","):
        number, color = cubes.strip().split(" ")
        if color == "red" and int(number) > 12:
            return False
        elif color == "green" and int(number) > 13:
            return False
        elif color == "blue" and int(number) > 14:
            return False
    return True

def part1():
    file = open('input.txt','r')
    output = 0
    for row in file:
        game, subsets = row.split(":")
        game = game.split(" ")[1]
        possibleGame = True
        for set in subsets.split(";"):
            possibleGame = countCubes(set)
            if possibleGame == False:
                break
        if possibleGame == True:
            output += int(game)
    print(output)

part1()