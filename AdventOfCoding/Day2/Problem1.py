

def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day2/input1.txt", "r") as f:
        return f.read().splitlines()


def check_possible(lines):
    color = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    res = 0
    for i, line in enumerate(lines):
        line = line.split(":")
        tmp = int(line[0][5:])
        add_tmp = False
        line[1] = line[1].split(";")
        for status in line[1]:
            status = status.replace(" ", "")
            status = status.split(",")
            for stat in status:
                if stat[0].isnumeric() and stat[1].isnumeric():
                    num = int(stat[:2])
                    if num > color[stat[2:]]:
                        add_tmp = True
                else:
                    num = int(stat[:1])
                    if num > color[stat[1:]]:
                        add_tmp = True
        if add_tmp is False:
            res += tmp

    return res


if __name__ == '__main__':
    lines = read_file()
    print(check_possible(lines))
