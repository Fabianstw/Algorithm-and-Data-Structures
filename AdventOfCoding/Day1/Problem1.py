
def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day1/inout1.txt", "r") as f:
        return f.readlines()


def read_lines(lines):
    res = 0
    for line in lines:
        tmp = []
        for i in range(len(line)):
            if line[i].isnumeric():
                tmp.append(line[i])
        res += int(tmp[0] + tmp[-1])
    return res

if __name__ == '__main__':
    line = read_file()
    print(read_lines(line))
