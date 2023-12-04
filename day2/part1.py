from utils.fileUtils import getLines

games = []

limits = {"red": 12, "green": 13, "blue": 14}


def solve_part1():
    games = [game.split(": ")[1] for game in getLines("input.txt")]
    impossibleGames = []
    for i in range(len(games)):
        sets = games[i].split("; ")
        for set in sets:
            for cube in set.split(", "):
                number = int(cube.split(" ")[0])
                color = cube.split(" ")[1]
                if limits[color] < number and not i + 1 in impossibleGames: impossibleGames.append(i + 1)
    print((len(games) * (len(games) + 1) // 2) - sum(impossibleGames))


def solve_part2():
    games = [game.split(": ")[1] for game in getLines("input.txt")]
    maxSets = []
    for i in range(len(games)):
        sets = games[i].split("; ")
        maxSets.append({'red': 0, 'blue': 0, 'green': 0})
        for set in sets:
            for cube in set.split(", "):
                number = int(cube.split(" ")[0])
                color = cube.split(" ")[1]
                if maxSets[i][color] < number: maxSets[i][color] = number
    powers = [maxSet['red'] * maxSet['green'] * maxSet['blue'] for maxSet in maxSets]
    print(sum(powers))


solve_part2()
