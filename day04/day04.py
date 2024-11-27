import os

filepath = os.path.abspath("day04/input.txt")
file = open(filepath)


def part1(file):
    sum = 0

    for line in file:
        line = line.strip()  # remove \n
        [card, data] = line.split(": ")
        [scratched, winning] = data.split(" | ")

        freq = {}
        count = 0

        for num in scratched.split(" "):
            if num == "":
                continue
            freq[num] = True

        for num in winning.split(" "):
            if num == "":
                continue
            if num in freq:
                count += 1

        if count > 0:
            sum += 2 ** (count - 1)

    return sum


print(part1(file))
