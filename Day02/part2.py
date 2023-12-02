def countCubes(set):
    ouputDict = {"red":0, "green":0, "blue":0}
    for cubes in set.split(","):
        number, color = cubes.strip().split(" ")
        if ouputDict[color] < int(number):
            ouputDict[color] = int(number)
    return ouputDict
    
def part2():
    file = open('input.txt','r')
    output = 0
    for row in file:
        subDict = {"red":0, "green":0, "blue":0}
        subsets = row.split(":")[1]
        for set in subsets.split(";"):
            tempDict = countCubes(set)
            for c in ["red", "green", "blue"]:
                if subDict.get(c) < tempDict.get(c):
                    subDict[c] = tempDict.get(c)
        output += subDict.get("red") * subDict.get("green") * subDict.get("blue")
    print(output)

part2()