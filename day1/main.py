from utils.fileUtils import getLines

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solve():
    lines = [line for line in getLines("input.txt")]

    # Replace each string values by numeric values
    for index_line in range(len(lines)):
        line = lines[index_line]
        finalLine = ""
        for i in range(len(line)):
            if any(line[i:].startswith(digit := item) for item in digits):
                finalLine += str(digits.index(digit) + 1)
            else:
                finalLine += line[i]
        lines[index_line] = finalLine

    # Replace everything except numbers
    lines = [''.join(filter(str.isdigit, line)) for line in lines]
    # Sum each first and last number in each line (if line is empty, add 0)
    s = sum(int(line[0] + line[-1]) if len(line) > 0 else 0 for line in lines)
    print(s)


solve()
