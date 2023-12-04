def read_file():
    with open \
                (
                "/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day3/input2.txt",
                "r") as f:
        return f.read().splitlines()


def calculate(lines):
    res = 0
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if lines[i][j] == "*":
                res += check_for_nums(lines, i, j)

    return res


def check_for_nums(lines, i, j):
    two_nums = []
    seen = set()
    for m in range(-1, 2):
        for n in range(-1, 2):
            if (i - m, j - n) not in seen:

                try:
                    if lines[i - m][j - n].isnumeric():
                        first = j - n
                        while lines[i - m][first].isnumeric():
                            first -= 1
                            if first < 0:
                                break
                        last = j - n
                        while lines[i - m][last].isnumeric():
                            last += 1
                            if last >= len(lines[i - m]):
                                break
                        for k in range(first + 1, last):
                            seen.add((i - m, k))
                        two_nums.append(int(lines[i - m][first + 1:last]))

                except IndexError:
                    pass

    tmp = 1
    if len(two_nums) == 2:

        for num in two_nums:
            tmp *= num
        return tmp
    print(two_nums)
    return 0


if __name__ == '__main__':
    print(calculate(read_file()))

    # 79687676 too low

    # 82689039 to high
