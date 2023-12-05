def part1():
    file = open('input.txt','r')
    output = 0
    for row in file:
        card, winners = row.split(":")[1].split("|")
        card = card.strip().split(" ")
        winners = winners.strip().split(" ")
        tempcount = 0
        print(card)
        print(winners)
        for n in card:
            if n == "":
                continue
            elif n in winners:
                if tempcount == 0:
                    tempcount = 1
                else:
                    tempcount *= 2
        print(tempcount)
        output += tempcount
    print(output)

part1()