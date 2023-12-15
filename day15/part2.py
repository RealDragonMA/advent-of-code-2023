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
    boxs = {i: {} for i in range(256)}
    for step in steps:
        key = step[:2]
        box_number = algorithm(key)
        operation = step[2]
        value = step[3:]
        if operation == "=":
            boxs[box_number][key] = int(value)
        elif operation == "-" and key in boxs[box_number]:
            del boxs[box_number][key]
    power = 0
    print(boxs)
    for box_number in boxs:
        box = box_number+1
        for lens in boxs[box_number]:
            index = list(boxs[box_number]).index(lens)+1
            power += box * index * boxs[box_number][lens]

    print(power)



solve()
