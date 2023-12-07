def part1():
    file = open('input.txt','r')
    time = []
    dist = []
    output = []
    for row in file:
        if "Time" in row:
            time = [int(x) for x in row.split(":")[1].strip().split(" ") if x != ""]
        else:
            dist = [int(x) for x in row.split(":")[1].strip().split(" ") if x != ""]
    print(time)
    print(dist)
    for i in range(len(time)):
        output.append(0)
        for t in range(time[i]):
            if t*(time[i]-t) > dist[i]:
                output[i] += 1

    result = 1
    for x in output:
        result = result * x
    print(result)

part1()