
def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day5/input1.txt", "r") as f:
        return f.read().splitlines()


def calculate(lines):

    res = 0
    map_d = dict()
    curr_matrix = []
    tmp_array = []
    for i, line in enumerate(lines):
        print(i)
        if i == 0:
            seeds = line
            seeds = seeds.replace("seeds: ", "")
            seeds = seeds.split(" ")
            print(seeds)
        elif i == 1:
            pass
        else:
            if len(line) == 0:
                new_dict = dict()
                for matrix in curr_matrix:
                    start, end, step = int(matrix[0]), int(matrix[1]), int(matrix[2])
                    for j in range(step):
                        new_dict.update({j+end: j+start})
                tmp_array.append(new_dict)
                curr_matrix = []
            elif line[0].isnumeric():
                tmp = line.split(" ")
                curr_matrix.append(tmp)

    new_dict = dict()
    for matrix in curr_matrix:
        start, end, step = int(matrix[0]), int(matrix[1]), int(matrix[2])
        for j in range(step):
            new_dict.update({j + end: j + start})
    tmp_array.append(new_dict)

    for t in tmp_array:
        print(t)

    res = []
    for seed in seeds:
        curr_value = int(seed)
        for tmp_a in tmp_array:
            if curr_value in tmp_a:
                curr_value = tmp_a[curr_value]

        res.append(curr_value)

    return min(res)


if __name__ == '__main__':
    print(calculate(read_file()))
