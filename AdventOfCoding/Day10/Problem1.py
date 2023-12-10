def read_file():
    with open(
        "/Users/fabianstiewe/Desktop/Coding/Github "
        "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day10/input1.txt",
        "r",
    ) as f:
        return f.read().splitlines()


def calc(lines):
    matrix = []
    start = None
    for i, line in enumerate(lines):
        new_row = []
        for j, lin in enumerate(line):
            if lin == "S":
                start = (i, j)
            new_row.append(lin)
        matrix.append(new_row)

    calc_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    calc_matrix[start[0]][start[1]] = 0

    queue = [(start[0]-1, start[1], 0), (start[0]+1, start[1], 0)]
    seen = set()
    seen.add(start)
    while queue:
        curr = queue.pop(0)
        checker = (curr[0], curr[1])
        if checker not in seen:
            seen.add(checker)
            calc_matrix[curr[0]][curr[1]] = curr[2] + 1
            if matrix[curr[0]][curr[1]] == "J":
                queue.append((curr[0] - 1, curr[1], curr[2] + 1))
                queue.append((curr[0], curr[1] - 1, curr[2] + 1))
            elif matrix[curr[0]][curr[1]] == "F":
                queue.append((curr[0] + 1, curr[1], curr[2] + 1))
                queue.append((curr[0], curr[1] + 1, curr[2] + 1))
            elif matrix[curr[0]][curr[1]] == "L":
                queue.append((curr[0] - 1, curr[1], curr[2] + 1))
                queue.append((curr[0], curr[1] + 1, curr[2] + 1))
            elif matrix[curr[0]][curr[1]] == "7":
                queue.append((curr[0] + 1, curr[1], curr[2] + 1))
                queue.append((curr[0], curr[1] - 1, curr[2] + 1))
            elif matrix[curr[0]][curr[1]] == "-":
                queue.append((curr[0], curr[1] + 1, curr[2] + 1))
                queue.append((curr[0], curr[1] - 1, curr[2] + 1))
            elif matrix[curr[0]][curr[1]] == "|":
                queue.append((curr[0] + 1, curr[1], curr[2] + 1))
                queue.append((curr[0] - 1, curr[1], curr[2] + 1))

    curr_max = 0
    for calc in calc_matrix:
        for cal in calc:
            if cal > curr_max:
                curr_max = cal
    return curr_max


if __name__ == '__main__':
    print(calc(read_file()))
