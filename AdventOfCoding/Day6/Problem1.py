def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day6/input1.txt", "r") as f:
        return f.read().splitlines()


def calc(lines):
    time, record = [], []
    time_tmp = lines[0]
    record_tmp = lines[1]
    time_tmp = time_tmp.split(" ")[1:]
    record_tmp = record_tmp.split(" ")[1:]
    for i, re in enumerate(record_tmp):
        if re != "":
            record.append(int(re))

    for ti in time_tmp:
        if ti != "":
            time.append(int(ti))

    res = 1
    for i, t in enumerate(time):
        count = 0
        for j in range(t):
            if j * (t-j) > record[i]:
                count += 1
        res *= count
    return res


if __name__ == '__main__':
    print(calc(read_file()))