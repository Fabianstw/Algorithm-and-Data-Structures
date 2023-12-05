def read_file():
    with open(
            "/Users/fabianstiewe/Desktop/Coding/Github "
            "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day4/input2.txt",
            "r") as f:
        return f.read().splitlines()


def calculate(lines):
    tmp = {x: 1 for x in range(len(lines))}

    for i, line in enumerate(lines):
        line = line.split(":")[1]
        line = line.split("|")
        winning = line[0]
        number = line[1]
        winning = winning.split(" ")
        number = number.split(" ")

        counter = -1
        for num in number:
            if num != "":
                if num in winning:
                    counter += 1

        for j in range(i+1, i+counter+2):
            tmp[j] += tmp[i]

    return sum(tmp.values())


if __name__ == '__main__':
    print(calculate(read_file()))

    # 79687676 too low

    # 82689039 to high
