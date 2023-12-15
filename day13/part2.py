def rotate(line):
    return [''.join(row) for row in zip(*reversed(line))]


def getReflection(pattern):
    ref = 0
    # 0 -> half
    for i in range(0, (len(pattern) // 2)):
        A = ''.join(pattern[:i + 1])
        B = ''.join(pattern[i + 1:2 * (i + 1)][::-1])
        difference = sum(A[i] != B[i] for i in range(len(A)))
        if difference == 1:
            if ref <= i:
                return i+1
    # half -> end
    for i in range((len(pattern) // 2) + 1, len(pattern)):
        A = ''.join(pattern[i - (len(pattern) - i):i])
        B = ''.join(pattern[i:][::-1])
        difference = sum(A[i] != B[i] for i in range(len(A)))
        if difference == 1:
            if ref <= i:
                return i+1
    return ref


def solve():
    patterns = [group.splitlines() for group in open("input.txt").read().split('\n\n')]
    rows = []
    columns = []
    for pattern in patterns:
        rows.append(getReflection(pattern))
        columns.append(getReflection(rotate(pattern)))
    print(rows)
    print(columns)
    print(sum(rows) * 100 + sum(columns))


solve()
