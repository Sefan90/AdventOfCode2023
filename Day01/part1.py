def part1():
    file = open('input.txt','r')
    output = 0
    for row in file:
        row_output = []
        for c in row:
            if c.isnumeric():
                row_output.append(c)
        output += int(row_output[0]+row_output[-1])
    print(output)

part1()