from utils.fileUtils import getLines
import re


def trouver_places(chaine, place_cherchee):
    regex = re.compile(r'([.?]|^)' + re.escape(place_cherchee) + r'([.?]|$)')
    return [m.start(0) for m in regex.finditer(chaine)]


def solve():
    lines = [(line.split(" ")[0], [int(v) for v in line.split(" ")[1].split(",")]) for line in getLines("input.txt")]
    for (line, values) in lines:
        
        print(re.findall(r"[?|.][?][?|.]", line), line)


solve()