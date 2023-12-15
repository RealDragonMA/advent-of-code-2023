import numpy as np

from utils.fileUtils import getLines


def rotate(line, rotations=1):
    return np.rot90(line, k=rotations)


def cycle(r):
    r = rotate([''.join("." * (len(interval) - interval.count("O")) + "O" * interval.count("O") + "#" for interval in line.split("#"))[:-1] for line in r])
    r = rotate([''.join("." * (len(interval) - interval.count("O")) + "O" * interval.count("O") + "#" for interval in line.split("#"))[:-1] for line in r])
    r = rotate([''.join("." * (len(interval) - interval.count("O")) + "O" * interval.count("O") + "#" for interval in line.split("#"))[:-1] for line in r])
    r = [''.join("." * (len(interval) - interval.count("O")) + "O" * interval.count("O") + "#" for interval in line.split("#"))[:-1] for line in r]
    return r
def solve():
    rotated = rotate(getLines("input.txt"))
    r = cycle(rotated)
    for i in range(1000000000-1):
        r = cycle(rotate(r))
    print(*r, sep="\n")
    print(sum(r[i].count("O") * (len(r) - i) for i in range(len(r))))



solve()
