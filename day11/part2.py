from utils.fileUtils import getLines

lines = []


def getDoubles():
    rows = [y for y in range(len(lines)) if all(c == "." for c in lines[y])]
    columns = [[row[x] for row in lines] for x in range(len(lines))]
    columns = [i for i in range(len(columns)) if all(c == "." for c in columns[i])]
    return rows, columns


def distance_entre_tuples(coord1, coord2, doubles):
    x1, y1 = coord1
    x2, y2 = coord2
    rows, columns = doubles
    expandRows = len([x for x in columns if x2 < x < x1 or x2 > x > x1])
    expandColumns = len([y for y in rows if y2 < y < y1 or y2 > y > y1])
    return (abs(x2 - x1)-expandColumns) + (abs(y2 - y1)-expandRows) + (expandColumns*1000000) + (expandRows*1000000)


def getGalaxies():
    coords = []
    for y in range(len(lines)):
        for x in range(len(lines)):
            if lines[y][x] == "#":
                coords.append((x, y))
    return coords


def solve():
    global lines
    lines = getLines("input.txt")
    doubles = getDoubles()
    galaxies = getGalaxies()
    c = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            c.append(distance_entre_tuples(galaxies[i], galaxies[j], doubles))
    print(sum(c))

solve()
