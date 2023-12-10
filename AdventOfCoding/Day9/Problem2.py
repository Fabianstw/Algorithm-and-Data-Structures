def read_file():
    with open(
        "/Users/fabianstiewe/Desktop/Coding/Github "
        "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day9/input1.txt",
        "r",
    ) as f:
        return f.read().splitlines()


def calc(lines):
    tmp_lst = []
    for line in lines:
        line = line.split(" ")
        tmp_lst.append(line)

    ans = 0
    for tmp in tmp_lst:
        calc_list = [tmp]

        counter = 0
        while True:
            curr_lst = calc_list[counter]
            new_lst = []
            only0 = True
            for i in range(len(curr_lst) - 1):
                new_lst.append(int(curr_lst[i + 1]) - int(curr_lst[i]))
                if new_lst[-1] != 0:
                    only0 = False

            calc_list.append(new_lst)
            if only0:
                break
            counter += 1

        for i in range(len(calc_list) - 1, 0, -1):  # to other for indexing
            calc_list[i - 1].insert(0, int(calc_list[i-1][0]) - int(calc_list[i][0]))

        ans += calc_list[0][0]

    return ans


if __name__ == "__main__":
    print(calc(read_file()))
