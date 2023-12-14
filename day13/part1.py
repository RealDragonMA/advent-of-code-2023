def rotate(line):
    return [list(row) for row in zip(*reversed(line))]


def getReflection(pattern):
    ref = []
    for i in range((len(pattern) // 2) + 1, len(pattern)):
        if pattern[i - (len(pattern) - i):i] == pattern[i:][::-1]:
            ref.append(i)
    return ref


def solve():
    patterns = [group.splitlines() for group in open("input.txt").read().split('\n\n')]
    rows = []
    columns = []
    for pattern in patterns:
        rows += getReflection(pattern)
        columns += getReflection(rotate(pattern))
    print(rows)
    print(columns)
    print(sum(rows)*100 + sum(columns))


solve()
