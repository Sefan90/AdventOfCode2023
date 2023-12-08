def part2():
    file = open('input.txt','r')
    inst = []
    map = {}
    inputvalues = []
    outputvalues = []
    output = 0
    counter = 0
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
    for key in map.keys():
        if key.endswith("A"):
            inputvalues.append(key)
            outputvalues.append(key[:2]+"Z")
    while inputvalues != outputvalues:
        for i in range(len(inputvalues)):
            inputvalues[i] = map.get(inputvalues[i])[inst[counter]]
        counter = (counter+1)%len(inst)
        output += 1
    print(inputvalues)
    print(output)


part2()