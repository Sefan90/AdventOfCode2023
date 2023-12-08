def part1():
    file = open('input.txt','r')
    inst = []
    map = {}
    output = 0
    for row in file:
        if row == "\n":
            continue
        elif "=" not in row:
            inst = [int(x.replace("R","1").replace("L","0")) for x in row.strip()]
        else:
            key, values = row.replace("(","").replace(")","").replace(" ","").replace("\n","").split("=")
            values = values.split(",")
            map[key] = values
    #print(inst)
    #print(map)
    inputvalue = "AAA"
    i = 0
    while inputvalue != "ZZZ":
        inputvalue = map.get(inputvalue)[inst[i]]
        i = (i+1)%len(inst)
        output += 1
        #print(inputvalue)
    print(output)


part1()