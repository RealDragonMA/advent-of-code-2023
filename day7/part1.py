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
    strengths = 'J23456789TQKA'
    return [strengths.index(char) for char in card[2]]


def solve():
    lines = getLines("input.txt")
    games = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
    ranks = sorted(strength(hand) for hand in games)
    sortedRanks = []
    for i in range(0, 7):
        ranksI = [r for r in ranks if r[0] == i]
        ranksI.sort(key=sort_power)
        sortedRanks += ranksI
    print(sortedRanks)
    s = sum((i + 1) * r[3] for i, r in enumerate(sortedRanks))
    print(s)


solve()
