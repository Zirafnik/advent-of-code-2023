import os

filepath = os.path.abspath("day03/input.txt")


def part1(data):
    sum = 0
    for i in range(len(data)):
        line = data[i]
        num = ""
        hasSymbol = False

        for j in range(len(line)):
            char = line[j]

            if char.isdigit():
                num += char

                if not hasSymbol:
                    # check all sides for a symbol (non-dot && non-digit)
                    if checkSurrCoords(i, j):
                        hasSymbol = True
            else:
                if hasSymbol:
                    sum += int(num)
                num = ""
                hasSymbol = False

            # If last number in line
            if j == len(line) - 1:
                if hasSymbol:
                    sum += int(num)

    return sum


def checkSurrCoords(lineIndex, charIndex):
    coordsToCheck = [
        [lineIndex - 1, charIndex - 1],
        [lineIndex - 1, charIndex],
        [lineIndex - 1, charIndex + 1],
        [lineIndex, charIndex - 1],
        [lineIndex, charIndex + 1],
        [lineIndex + 1, charIndex - 1],
        [lineIndex + 1, charIndex],
        [lineIndex + 1, charIndex + 1],
    ]

    for coords in coordsToCheck:
        try:
            if coords[0] >= 0 and coords[1] >= 0:
                line = data[coords[0]]
                char = line[coords[1]]

                if not char.isdigit() and char != ".":
                    return True
        except IndexError:
            continue

    return False


def part2(data):
    gearNums = {}

    for i in range(len(data)):
        line = data[i]
        num = ""
        gears = set()

        for j in range(len(line)):
            char = line[j]

            if char.isdigit():
                num += char

                # check all sides for a gear
                gearCoords = checkForGearCoords(i, j)
                gears.update(gearCoords)
            else:
                if len(gears):
                    for gear in gears:
                        gearNums.setdefault(gear, []).append(int(num))
                num = ""
                gears = set()

    # Calculate and sum all gear ratios where there are two (or more) part numbers
    gearRatioSum = 0
    for gear in gearNums:
        if len(gearNums[gear]) >= 2:
            gearRatio = 1
            for num in gearNums[gear]:
                gearRatio *= num

            gearRatioSum += gearRatio

    return gearRatioSum


def checkForGearCoords(lineIndex, charIndex):
    gears = []

    coordsToCheck = [
        [lineIndex - 1, charIndex - 1],
        [lineIndex - 1, charIndex],
        [lineIndex - 1, charIndex + 1],
        [lineIndex, charIndex - 1],
        [lineIndex, charIndex + 1],
        [lineIndex + 1, charIndex - 1],
        [lineIndex + 1, charIndex],
        [lineIndex + 1, charIndex + 1],
    ]

    for coords in coordsToCheck:
        try:
            if coords[0] >= 0 and coords[1] >= 0:
                line = data[coords[0]]
                char = line[coords[1]]

                if char == "*":
                    gears.append((coords[0], coords[1]))
        except IndexError:
            continue

    return gears


with open(filepath) as file:
    data = file.read().splitlines()

    print(part2(data))
