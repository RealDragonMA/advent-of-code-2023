from utils.fileUtils import getLines


def algorithm(text):
    s = 0
    for x in text:
        s += ord(x)
        s *= 17
        s %= 256
    return s


def solve():
    steps = [step for step in getLines("input.txt")[0].split(",")]
    print(steps)
    print(sum(algorithm(step) for step in steps))


solve()
