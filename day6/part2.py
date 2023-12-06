from utils.fileUtils import getLines


def solve():
    lines = getLines("input.txt")
    time = int(''.join(word for word in lines[0].split() if word.isdigit()))
    distance = int(''.join(word for word in lines[1].split() if word.isdigit()))
    winning = [[ms for ms in range(1, time + 1) if ms * (time - ms) > distance]]
    s = 1
    for win in winning:
        s *= len(win)
    print(s)


solve()
