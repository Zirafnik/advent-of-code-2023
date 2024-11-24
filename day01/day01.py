file = open('input.txt')

# Time: O(n*m) where n is number of lines & m is length of line
# Space: O(1) or O(n) where n is length of line
def part1():
    sum = 0
    for line in file:
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
            
        finalDigit = int(first + second)
        sum += finalDigit
    
    return sum

def part2():
    sum = 0
    for line in file:
        None
    return sum


print(part1())