from utils.fileUtils import getLines


def explode(node):
    key = node.split(" = ")[0]
    values = node.split(" = ")[1].replace(" ", "").replace("(", "").replace(")", "").split(",")
    left = values[0]
    right = values[1]
    return key, left, right


def solve():
    lines = getLines("input.txt")
    steps = [step for step in lines[0]]
    nodes = lines[2:]
    d = {key: {"L": left, "R": right} for key, left, right in (explode(node) for node in nodes)}
    currentStep, cursorStep = 'AAA', 0
    totalStep = 0
    while currentStep != 'ZZZ':
        currentStep = d[currentStep][steps[cursorStep]]
        cursorStep = (cursorStep + 1) % len(steps)
        totalStep += 1
    print(totalStep)


solve()
