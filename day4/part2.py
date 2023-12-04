from utils.fileUtils import getLines


def getMatching(games, nb):
    same = []
    for game in games:
        spliter = game.split(": ")
        nbGame = int(spliter[0].split(" ")[-1])
        if nbGame != nb:
            continue
        gameInfos = spliter[1]
        winning = [int(x) for x in gameInfos.split(" | ")[0].split(" ") if x != ""]
        mine = [int(x) for x in gameInfos.split(" | ")[1].split(" ") if x != ""]
        same = [el for el in winning if el in mine]
    return len(same)


def solve():
    games = getLines("input.txt")
    tab = [1] * len(games)
    for i in range(len(games)):
        cardS = getMatching(games, i+1)
        print(cardS)
        for j in range(i + 1, i + cardS + 1):
            tab[j] += 1 * tab[i]
    print(sum(tab))

solve()
