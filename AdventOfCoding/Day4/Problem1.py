

def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/AdventOfCoding/Day4/input1.txt", "r") as f:
        return f.read().splitlines()


def calculate(lines):
    res = 0
    for line in lines:
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
        if counter != -1:
            res += 2**counter
    return res


if __name__ == '__main__':
    print(calculate(read_file()))
