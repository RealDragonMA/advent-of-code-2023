from utils.fileUtils import getLines


def solve():
    games = [game.split(": ")[1] for game in getLines("input.txt")]
    total = 0
    for game in games:
        winning = [int(x) for x in game.split(" | ")[0].split(" ") if x != ""]
        mine = [int(x) for x in game.split(" | ")[1].split(" ") if x != ""]
        same = [el for el in winning if el in mine]
        total += 0 if len(same) == 0 else 2 ** (len(same) - 1)
    print(total)


solve()
