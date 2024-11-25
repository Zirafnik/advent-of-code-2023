import os

filepath = os.path.abspath("day01/test2.txt")
file = open(filepath)


# Time: O(n) where n is length of line
# Space: O(1)
# Note: We could probably have two pointers (start & end) to optimize a bit
def getFinalDigits(line):
    first = None
    second = None

    for char in line:
        # check if numeric
        if char.isdigit():
            # if first = None, set both
            if first is None:
                first = char
                second = char
            # else just set second
            else:
                second = char

    # Edge case w/ no numbers in string
    finalDigit = int((first or 0) + (second or 0))

    return finalDigit


# Time: O(n*m) where n is number of lines & m is length of line
# Space: O(1) or O(n) where n is length of line
def part1():
    sum = 0
    for line in file:
        finalDigit = getFinalDigits(line)
        sum += finalDigit

    return sum


# Time: O(n*m) where is n is the number of lines & m is length of line
# Space: O(1) or O(n) where n is length of line
def part2():
    # Two numbers share at most 1 letter end/beginning, so we keep first & last char for overlapping numbers
    numWords = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    sum = 0
    for line in file:
        # Constant O(9) due to constant number of keys
        for key in numWords:
            # O(n) because we loop over each string to replace chars (line.replace() is O(n) as it uses KMP in background)
            line = line.replace(key, numWords[key])

        finalInt = getFinalDigits(line)
        sum += finalInt

    return sum


print(part1())
print(part2())
