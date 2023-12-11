from utils.fileUtils import getLines

lines = []

d = {
    "|": {
        "L": [],
        "R": [],
        "D": ["J", "L", "|", "S"],
        "U": ["7", "F", "|", "S"]
    },
    "L": {
        "L": [],
        "R": ["-", "7", "J", "S"],
        "D": [],
        "U": ["7", "|", "F", "S"]
    },
    "J": {
        "L": ["-", "F", "L", "S"],
        "R": [],
        "D": [],
        "U": ["|", "7", "F", "S"]
    },
    "7": {
        "L": ["-", "F", "L", "S"],
        "R": [],
        "D": ["|", "L", "J", "S"],
        "U": []
    },
    "F": {
        "L": [],
        "R": ["7", "-", "J", "S"],
        "D": ["|", "J", "L", "S"],
        "U": []
    },
    "-": {
        "L": ["L", "-", "F", "S"],
        "R": ["7", "-", "J", "S"],
        "D": [],
        "U": []
    },
    "S": {
        "L": ["L", "-", "F"],
        "R": ["-", "7", "J"],
        "D": ["|", "L", "J"],
        "U": ["|", "7", "F"]
    }
}


def getPossible(coord):
    x, y = coord
    possibles = []
    symbol = getSymbol(coord)
    if symbol == ".":
        return []
    directions = {
        "L": (x - 1, y),
        "R": (x + 1, y),
        "D": (x, y + 1),
        "U": (x, y - 1)
    }
    for direction in directions:
        _coord = directions[direction]
        _symbol = str(getSymbol(_coord))
        if _symbol in d[symbol][direction] and direction not in possibles:
            possibles.append(direction)
    return possibles


def getSymbol(coord):
    x, y = coord
    if x < 0 or x > len(lines[0]) - 1 or y < 0 or y > len(lines) - 1:
        return "."
    return lines[y][x]


def reverse(direction):
    directions = {
        "L": "R",
        "D": "U",
        "R": "L",
        "U": "D"
    }
    return directions[direction]


def getNext(coord, direction):
    x, y = coord
    directions = {
        "L": (x - 1, y),
        "R": (x + 1, y),
        "D": (x, y + 1),
        "U": (x, y - 1)
    }
    return directions[direction]


def getStarting():
    for y in range(0, len(lines)):
        for x in range(0, len(lines)):
            if getSymbol((x, y)) == 'S':
                return x, y


def solve():
    global lines
    lines = getLines("input.txt")
    s_coords = getStarting()
    directions = getPossible(s_coords)
    roads = []
    for dir in directions:
        moves = []
        currentCoord = getNext(s_coords, dir)
        direction = dir
        while getSymbol(currentCoord) != "S":
            possibles = getPossible(currentCoord)
            possibles.remove(reverse(direction))
            if len(possibles) == 0:
                break
            direction = possibles[0]
            currentCoord = getNext(currentCoord, direction)
            moves.append(currentCoord)
        roads.append(moves)
    print((len(max(roads, key=len))+1)/2)


solve()
