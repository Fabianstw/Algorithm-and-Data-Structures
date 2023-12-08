def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day6/input1.txt", "r") as f:
        return f.read().splitlines()


def calc(lines):
    time, record = "", ""
    time_tmp = lines[0]
    record_tmp = lines[1]
    time_tmp = time_tmp.split(" ")[1:]
    record_tmp = record_tmp.split(" ")[1:]
    for i, re in enumerate(record_tmp):
        if re != "":
            record += re

    for ti in time_tmp:
        if ti != "":
            time += ti

    # make this via binary search
    count = 0

    left, right = 0, int(time)//2
    while left < right:
        mid = (left + right) // 2
        if mid * (int(time)-mid) > int(record):
            right = mid - 1
        else:
            left = mid + 1

    count = left

    left, right = int(time)//2, int(time)
    while left < right:
        mid = (left + right) // 2
        if mid * (int(time)-mid) > int(record):
            left = mid + 1
        else:
            right = mid - 1
    count += (int(time) - right)



    return int(time) - count + 1


if __name__ == '__main__':
    print(calc(read_file()))