from utils.fileUtils import getLines
from math import gcd


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
    dA = [key for key in d.keys() if key.endswith('A')]
    currentSteps, cursorStep = dA, 0
    totalSteps = []
    for i in range(len(currentSteps)):
        totalStep = 0
        while not currentSteps[i].endswith("Z"):
            currentSteps[i] = d[currentSteps[i]][steps[cursorStep]]
            cursorStep = (cursorStep + 1) % len(steps)
            totalStep += 1
        totalSteps.append(totalStep)
    print(totalSteps)
    lcm = 1
    for i in totalSteps:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)


solve()
