from utils.fileUtils import getLines

lines = []


def getMaps(type):
    stsLine = lines.index(f"{type} map:")
    converter = []
    while stsLine + 1 < len(lines) and lines[stsLine + 1] != "":
        converter.append([int(x) for x in lines[stsLine + 1].split(" ")])
        stsLine += 1
    return converter


def getSeedTo(seed, maps):
    s = seed
    for destRangeStart, srcRangeStart, length in maps:
        if srcRangeStart <= seed <= srcRangeStart + length - 1:
            s = destRangeStart + (seed - srcRangeStart)
    return s


def seedToSoil(seed):
    s = seed
    maps = getMaps("seed-to-soil")
    return getSeedTo(s, maps)


def soilToFertilizer(seed):
    s = seed
    maps = getMaps("soil-to-fertilizer")
    return getSeedTo(s, maps)


def fertilizerToWater(seed):
    s = seed
    maps = getMaps("fertilizer-to-water")
    return getSeedTo(s, maps)


def waterToLight(seed):
    s = seed
    maps = getMaps("water-to-light")
    return getSeedTo(s, maps)


def lightToTemperature(seed):
    s = seed
    maps = getMaps("light-to-temperature")
    return getSeedTo(s, maps)


def temperatureToHumidity(seed):
    s = seed
    maps = getMaps("temperature-to-humidity")
    return getSeedTo(s, maps)


def humidityToLocation(seed):
    s = seed
    maps = getMaps("humidity-to-location")
    return getSeedTo(s, maps)


def seedToLocation(seed):
    return humidityToLocation(
        temperatureToHumidity(lightToTemperature(waterToLight(fertilizerToWater(soilToFertilizer(seedToSoil(seed)))))))


def solve():
    global lines
    lines = getLines("input.txt")
    seeds = [int(seed) for seed in lines[0].split(": ")[1].split(" ")]
    m = 100000000000000000000000
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i], seeds[i+1]):
            s = seedToLocation(j)
            if m > s: m = s
    print(m)


solve()
