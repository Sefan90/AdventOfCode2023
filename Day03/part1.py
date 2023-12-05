numbers = ["0","1","2","3","4","5","6","7","8","9"]

def createnumber(engine,x,y,i,j):
    temp_j = 1
    number1 = ""

    while y+j+temp_j < len(engine[x+i]) and engine[x+i][y+j+temp_j] in numbers:
        number1 += engine[x+i][y+j+temp_j]
        temp_j += 1
    
    temp_j = 0
    number2 = ""

    while engine[x+i][y+j+temp_j] in numbers:
        number2 = engine[x+i][y+j+temp_j] + number2
        temp_j -= 1

    return int(number2+number1)


def findnumber(engine,x,y):
    output_numbers = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            elif engine[x+i][y+j] in numbers:
                output_numbers.append(createnumber(engine,x,y,i,j))
    return list(set(output_numbers))

def part1():
    file = open('input.txt','r')
    output = []
    engine = [c for c in [row.strip() for row in file]]
    for x, row in enumerate(engine):
        for y, c in enumerate(row):
            if c not in ["0","1","2","3","4","5","6","7","8","9","."]:
                output.extend(findnumber(engine,x,y))

    print(output)
    print(sum(output))

part1()