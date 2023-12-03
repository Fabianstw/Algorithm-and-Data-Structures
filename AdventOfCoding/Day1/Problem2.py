

def read_lines():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day1/input2.txt", "r") as f:
        return f.readlines()


def read_input(lines):
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"}

    res = 0

    for line in lines:
        tmp = []
        while len(line) > 1:
            if line[0].isnumeric():
                tmp.append(line[0])
                line = line[1:]
                continue
            for num in numbers:
                if line.startswith(num):
                    tmp.append(numbers[num])
                    break
            line = line[1:]
        res += int(tmp[0] + tmp[-1])
    return res


if __name__ == '__main__':
    print(read_input(read_lines()))
