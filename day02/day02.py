import os

filepath = os.path.abspath("day02/input.txt")
file = open(filepath)

maxCubeNums = {"red": 12, "green": 13, "blue": 14}


def part1():
    sumOfIDs = 0

    for line in file:
        [game, sets] = line.rstrip().split(": ")
        gameId = game.split(" ")[-1]

        setsArr = sets.split("; ")

        gamePossible = True
        for set in setsArr:
            if gamePossible == False:
                break

            items = set.split(", ")

            for item in items:
                [num, color] = item.split(" ")

                if int(num) <= maxCubeNums[color]:
                    continue
                else:
                    gamePossible = False
                    break

        if gamePossible:
            sumOfIDs += int(gameId)

    return sumOfIDs


def part2():
    sumOfSetPowers = 0

    for line in file:
        [game, sets] = line.rstrip().split(": ")

        setsArr = sets.split("; ")

        maxCubeCounts = {"red": 0, "green": 0, "blue": 0}

        for set in setsArr:
            items = set.split(", ")

            for item in items:
                [num, color] = item.split(" ")

                maxCubeCounts[color] = max(maxCubeCounts[color], int(num))

        setPower = maxCubeCounts["red"] * maxCubeCounts["green"] * maxCubeCounts["blue"]

        sumOfSetPowers += setPower

    return sumOfSetPowers


# print(part1())
print(part2())
