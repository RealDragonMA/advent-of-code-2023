from utils.fileUtils import getLines


def solve():
    lines = [[int(x) for x in line.split(" ")][::-1] for line in getLines("input.txt")]
    s = 0
    for line in lines:
        sequence = [line]
        while not all(element == 0 for element in sequence[-1]):
            sequence.append([b - a for a, b in zip(sequence[-1], sequence[-1][1:])])
        sequence = sequence[::-1]
        for seq in sequence:
            seq.append(seq[-1])
        for i in range(1, len(sequence)):
            sequence[i][-1] += sequence[i - 1][-1]
        print(sequence)
        s += sequence[-1][-1]
    print(s)


solve()
