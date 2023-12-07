def part2():
    file = open('input.txt','r')
    time = 0
    dist = 0
    output = 0
    for row in file:
        if "Time" in row:
            time = int(row.split(":")[1].replace(" ",""))
        else:
            dist = int(row.split(":")[1].replace(" ",""))
    print(time)
    print(dist)
    for t in range(time):
        if t*(time-t) > dist:
            output += 1

    print(output)

part2()