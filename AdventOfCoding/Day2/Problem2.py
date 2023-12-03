

def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day2/input2.txt", "r") as f:
        return f.read().splitlines()


def check_possible(lines):

    res = 0
    for i, line in enumerate(lines):
        color = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        line = line.split(":")
        line[1] = line[1].split(";")
        for status in line[1]:
            status = status.replace(" ", "")
            status = status.split(",")
            for stat in status:
                if stat[0].isnumeric() and stat[1].isnumeric():
                    num = int(stat[:2])
                    if num > color[stat[2:]]:
                        color[stat[2:]] = num
                else:
                    num = int(stat[:1])
                    if num > color[stat[1:]]:
                        color[stat[1:]] = num

        print(color["red"]*color["blue"]*color["green"])
        res += color["red"]*color["blue"]*color["green"]

    return res


if __name__ == '__main__':
    lines = read_file()
    print(check_possible(lines))
