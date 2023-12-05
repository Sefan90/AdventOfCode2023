def part2():
    file = open('input.txt','r')
    noofcopys = [1 for row in file]
    file = open('input.txt','r')
    for i, row in enumerate(file):
        temp_i = 1
        card, winners = row.split(":")[1].split("|")
        card = card.strip().split(" ")
        winners = winners.strip().split(" ")
        for n in card:
            if n == "":
                continue
            elif n in winners:
                noofcopys[i+temp_i] += noofcopys[i]
                temp_i += 1
    print(sum(noofcopys))

part2()