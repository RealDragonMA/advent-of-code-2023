def getLines(file):
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines
