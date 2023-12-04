

def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day3/input1.txt", "r") as f:
        return f.read().splitlines()


def calculate(lines):
    res = 0
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            if line[j].isnumeric():
                first = j
                while line[j].isnumeric() and j < len(line):
                    j += 1
                    if j == len(line):
                        break
                if check_for_symbol(lines, first, j, i):
                    res += int(line[first:j])
            else:
                j += 1

    return res


def check_for_symbol(lines, start, end, line):
    for m in range(start-1, end+1):
        if line > 0 and 0 <= m < len(lines[0]):
            if lines[line-1][m] != "." and not lines[line-1][m].isnumeric():
                return True
        if line < len(lines)-1 and 0 <= m < len(lines[0]):
            if lines[line+1][m] != "." and not lines[line+1][m].isnumeric():
                return True
    if start > 0:
        if lines[line][start-1] != "." and not lines[line][start-1].isnumeric():
            return True
    if end < len(lines)-1:
        if lines[line][end] != "." and not lines[line][end].isnumeric():
            return True
    return False


if __name__ == '__main__':
    print(calculate(read_file()))
