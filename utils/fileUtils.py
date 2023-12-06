def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines
