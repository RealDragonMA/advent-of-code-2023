from utils.fileUtils import getLines

schematic = []


def getSymbol(x, y):
    if x < 0 or x > len(schematic[0]) - 1 or y < 0 or y > len(schematic) - 1:
        return "."
    return schematic[y][x]


def isValid(x, y):
    neighbors = [getSymbol(x + 1, y), getSymbol(x - 1, y), getSymbol(x, y + 1), getSymbol(x, y - 1),
                 getSymbol(x + 1, y - 1), getSymbol(x + 1, y + 1), getSymbol(x - 1, y - 1), getSymbol(x - 1, y + 1)]
    return any(
        symbol in neighbors for symbol in
        ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', '\\',
         ':', ';', '"', '\'', '<', ',', '>', '?', '/'])


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
    valids = []
    validsCoords = []
    # Retrieve the coords of each symbols
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            value, start, end = getNumber(x, y)
            if value == 0: continue
            valid = False
            for cx in range(start, end + 1):
                valid |= isValid(cx, y)
            if valid and not (start, y) in validsCoords:
                valids.append(value)
                validsCoords.append((start, y))
    sumValids = sum(int(x) for x in valids)
    print(sumValids)


solve()
