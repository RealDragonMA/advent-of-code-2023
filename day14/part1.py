from utils.fileUtils import getLines


def rotate(line):
    return [''.join(row) for row in zip(*reversed(line))]


def solve():
    rotated = rotate(getLines("input.txt"))
    north = [''.join("." * (len(interval) - interval.count("O")) + "O" * interval.count("O") + "#" for interval in line.split("#"))for line in rotated]
    north = rotate(rotate(rotate(north)))[1:]
    print(sum(north[i].count("O") * (len(north) - i) for i in range(len(north))))


solve()
