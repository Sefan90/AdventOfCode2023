def strnumber(input_str):
    for j, w in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        if input_str.find(w) == 0:
            return j+1
    return -1
    
def part2():
    file = open('input.txt','r')
    output = 0
    i = 0
    for row in file:
        row_output = []
        for i, c in enumerate(row):
            if c.isnumeric():
                row_output.append(c)
            else:
                tmp = strnumber(row[i:])
                if tmp != -1:
                    row_output.append(str(tmp))
        output += int(row_output[0]+row_output[-1])
    print(output)

part2()