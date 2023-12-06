from utils.fileUtils import getLines


def solve():
    lines = getLines("input.txt")
    times = [int(word) for word in lines[0].split() if word.isdigit()]
    distance = [int(word) for word in lines[1].split() if word.isdigit()]
    data = [(int(times[i]), int(distance[i])) for i in range(len(times))]
    winning = [[ms for ms in range(1, time + 1) if ms * (time - ms) > distance] for (time, distance) in data]
    s = 1
    for win in winning:
        s *= len(win)
    print(s)


solve()
