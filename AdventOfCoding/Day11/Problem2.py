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
            rows.append(i)
        matrix.append(list(line))

    for i in range(len(lines[0])):
        otherDot = False
        for j in range(len(lines)):
            if lines[j][i] != ".":
                otherDot = True
        if not otherDot:
            cols.append(i)

    starts = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                starts.append((i, j))

    print(starts)
    ans = 0
    for i in range(len(starts)):
        for j in range(i+1, len(starts)):
            # get amount of numbers in cols between starts[i][1] and starts[j][1]
            tmp1 = 0
            for value in cols:
                if starts[i][1] < value < starts[j][1]:
                    tmp1 += 999999
                if starts[j][1] < value < starts[i][1]:
                    tmp1 += 999999
            for value in rows:
                if starts[i][0] < value < starts[j][0]:
                    tmp1 += 999999
                if starts[j][0] < value < starts[i][0]:
                    tmp1 += 999999
            print(starts[i], starts[j])
            print(abs(starts[i][0]-starts[j][0]) + abs(starts[i][1]-starts[j][1]) + tmp1)
            ans += abs(starts[i][0]-starts[j][0]) + abs(starts[i][1]-starts[j][1]) + tmp1

    return ans


if __name__ == "__main__":
    print(calc(read_file()))
