from utils.fileUtils import getLines

schematic = []


def getSymbol(x, y):
    if x < 0 or x > len(schematic[0]) - 1 or y < 0 or y > len(schematic) - 1:
        return "."
    return schematic[y][x]


def neighbors(x, y):
    g = getNumber
    n = [g(x + 1, y), g(x - 1, y), g(x, y + 1), g(x, y - 1), g(x + 1, y - 1), g(x + 1, y + 1), g(x - 1, y - 1),
         g(x - 1, y + 1)]
    res = []
    for x in n:
        if x != (0, 0, 0): res.append(x)
    return set(res)


def getNumber(x, y):
    if not getSymbol(x, y).isdigit():
        return 0, 0, 0
    value = getSymbol(x, y)
    left = x - 1
    right = x + 1
    while getSymbol(left, y).isdigit():
        value = getSymbol(left, y) + value
        left -= 1
    while getSymbol(right, y).isdigit():
        value = value + getSymbol(right, y)
        right += 1
    return value, left + 1, right - 1


def solve():
    global schematic
    schematic = getLines("input.txt")
    engineCoords = []
    # Retrieve the coords of each symbols
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if getSymbol(x, y) == "*":
                engineCoords.append((x, y))
    s = 0
    for x, y in engineCoords:
        n = [int(x[0]) for x in list(neighbors(x, y))]
        if len(list(n)) < 2: continue
        s += n[0] * n[1]
    print(s)


solve()
