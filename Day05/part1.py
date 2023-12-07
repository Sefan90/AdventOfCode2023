def part1():
    file = open('input.txt','r')
    counterlist = []
    seedlist = []
    counter = 0
    output = 0
    for row in file:
        if "seeds" in row:
            seedlist = [int(x) for x in row.split(":")[1].strip().split(" ")]
            counterlist = [0 for _ in seedlist]
        else:
            if "map" in row:
                counterlist = [counter for _ in counterlist]
                counter += 1
            elif row != "\n":
                for i, seed in enumerate(seedlist):
                    if counterlist[i] < counter:
                        dest, source, length = [int(x) for x in row.strip().split(" ")]
                        if seed in range(source, source+length):
                            seedlist[i] = seedlist[i]-source+dest
                            counterlist[i] += 1
                        


    print(min(seedlist))

part1()