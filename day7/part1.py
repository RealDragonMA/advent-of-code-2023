from utils.fileUtils import getLines


def strength(game):
    hand = game[0]
    bid = game[1]
    s = len(set(hand))
    d = {card: hand.count(card) for card in set(hand)}
    return {
        s == 5: (0, "High card", hand, bid),
        s == 4: (1, "One pair", hand, bid),
        s == 3 and max(d.values()) == 2: (2, "Two pair", hand, bid),
        s == 3 and max(d.values()) == 3: (3, "Three of a kind", hand, bid),
        s == 2 and max(d.values()) == 3: (4, "Full house", hand, bid),
        s == 2 and max(d.values()) == 4: (5, "Four of a kind", hand, bid),
        s == 1: (6, "Five of a kind", hand, bid)
    }[True]


def sort_power(card):
    strengths = '23456789TJQKA'
    return [strengths.index(char) for char in card[2]]


def solve():
    lines = getLines("input.txt")
    games = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
    ranks = sorted(strength(hand) for hand in games)
    sortedRanks = []
    for i in range(6):
        # List of same power games with i
        ranksI = list(x for x in filter(lambda x: x[0] == i, ranks))
        sortedRanks += sorted(ranksI, key=sort_power)
    print(sortedRanks)
    s = 0
    for i in range(len(sortedRanks)):
        print(sortedRanks[i])
        s += (i+1) * sortedRanks[i][3]
    print(s)


solve()
