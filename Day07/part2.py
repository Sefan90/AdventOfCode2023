def part2():
    file = open('input.txt','r')
    cards = []
    bid = []
    hands = [[],[],[],[],[],[],[]]
    for row in file:
        cards.append(row.split(" ")[0])
        bid.append(int(row.split(" ")[1]))

    for i in range(len(cards)):
        tempcard = list(set(list(cards[i])))
        if cards[i].count("J") >= 4:
            hands[0].append(cards[i])
        elif cards[i].count("J") == 3:
            if len(tempcard) == 2:
                hands[0].append(cards[i])
            else:
                hands[1].append(cards[i])
        elif cards[i].count("J") == 2:
            if len(tempcard) == 2:
                hands[0].append(cards[i])
            elif len(tempcard) == 3:
                hands[1].append(cards[i])
            else:
                hands[3].append(cards[i])
        elif cards[i].count("J") == 1:
            if len(tempcard) == 1:
                hands[0].append(cards[i])
            elif len(tempcard) == 5:
                hands[5].append(cards[i])
            else:
                handsfound = 0
                for t in tempcard:
                    if cards[i].count(t) == 4:
                        hands[0].append(cards[i])
                        break
                    elif cards[i].count(t) == 3:
                        if handsfound == 2:
                            handsfound += 3
                            break
                        handsfound = 3
                    elif cards[i].count(t) == 2:
                        if handsfound == 3 or handsfound == 2:
                            handsfound += 2
                            break
                        handsfound = 2
                if handsfound == 2:
                    hands[3].append(cards[i])
                elif handsfound == 3:
                    hands[1].append(cards[i])
                elif handsfound == 4:
                    hands[2].append(cards[i])
                elif handsfound == 5:
                    hands[1].append(cards[i])
        else:
            if len(tempcard) == 1:
                hands[0].append(cards[i])
            elif len(tempcard) == 5:
                hands[6].append(cards[i])
            else:
                handsfound = 0
                for t in tempcard:
                    if cards[i].count(t) == 4:
                        hands[1].append(cards[i])
                        break
                    elif cards[i].count(t) == 3:
                        if handsfound == 2:
                            handsfound += 3
                            break
                        handsfound = 3
                    elif cards[i].count(t) == 2:
                        if handsfound == 3 or handsfound == 2:
                            handsfound += 2
                            break
                        handsfound = 2
                if handsfound == 2:
                    hands[5].append(cards[i])
                elif handsfound == 3:
                    hands[3].append(cards[i])
                elif handsfound == 4:
                    hands[4].append(cards[i])
                elif handsfound == 5:
                    hands[2].append(cards[i])

    SORT_ORDER = {"A":1, "K":2, "Q":3, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12, "J":13}
    for hand in hands:
        hand.sort(key=lambda val: SORT_ORDER[val[0]]*38416+SORT_ORDER[val[1]]*2744+SORT_ORDER[val[2]]*196+SORT_ORDER[val[3]]*14+SORT_ORDER[val[4]])
        outputorder = hands[0]+hands[1]+hands[2]+hands[3]+hands[4]+hands[5]+hands[6]
        output = 0
    outputorder.reverse()
    for i, hand in enumerate(outputorder):
        output += bid[cards.index(hand)]*(i+1)

    print(output)
part2()
