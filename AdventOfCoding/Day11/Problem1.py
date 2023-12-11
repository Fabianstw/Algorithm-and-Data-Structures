def read_file():
    with open(
        "/Users/fabianstiewe/Desktop/Coding/Github "
        "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day11/input1.txt",
        "r",
    ) as f:
        return f.read().splitlines()


def calc(lines):
    matrix = []
    cols, rows = [], []
    for i, line in enumerate(lines):
        if line.count(".") == len(line):
            matrix.append(list(line))
            matrix.append(list(line))
        else:
            matrix.append(list(line))

    for i in range(len(lines[0])):
        otherDot = False
        for j in range(len(lines)):
            if lines[j][i] != ".":
                otherDot = True
        if not otherDot:
            cols.append(i)

    print(cols)
    length = len(lines[0])
    for i in range(len(matrix)):
        for j in range(length):
            if j in cols:
                matrix[i].insert(j+cols.index(j), ".")

    for ma in matrix:
        print(ma)
    starts = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                starts.append((i, j))

    ans = 0
    for i in range(len(starts)):
        for j in range(i+1, len(starts)):
            print(starts[i], starts[j])
            print(abs(starts[i][0]-starts[j][0]) + abs(starts[i][1]-starts[j][1]))
            ans += abs(starts[i][0]-starts[j][0]) + abs(starts[i][1]-starts[j][1])

    return ans


if __name__ == "__main__":
    print(calc(read_file()))
