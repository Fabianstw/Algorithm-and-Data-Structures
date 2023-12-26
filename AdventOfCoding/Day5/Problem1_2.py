
def read_file():
    with open("/Users/fabianstiewe/Desktop/Coding/Github "
              "Public/Algorithm-and-Data-Structures/AdventOfCoding/Day5/input1.txt", "r") as f:
        return f.read().splitlines()


def calculate(lines):

    curr_matrix = []
    tmp_array = []
    for i, line in enumerate(lines):
        if i == 0:
            seeds = line
            seeds = seeds.replace("seeds: ", "")
            seeds = seeds.split(" ")
            print(seeds)
        elif i == 1:
            pass
        else:
            if len(line) == 0:
                new_matrix = []
                for matrix in curr_matrix:
                    new_matrix.append([int(matrix[0]), int(matrix[1]), int(matrix[2])])
                tmp_array.append(new_matrix)
                curr_matrix = []
            elif line[0].isnumeric():
                tmp = line.split(" ")
                curr_matrix.append(tmp)

    new_matrix = []
    for matrix in curr_matrix:
        new_matrix.append([int(matrix[0]), int(matrix[1]), int(matrix[2])])
    tmp_array.append(new_matrix)


    res = []
    for seed in seeds:
        curr_value = int(seed)
        for i in range(len(tmp_array)):
            for j in range(len(tmp_array[i])):
                if int(tmp_array[i][j][1]) <= curr_value < int(tmp_array[i][j][1]) + int(tmp_array[i][j][2]):
                    curr_value = curr_value + (int(tmp_array[i][j][0])- int(tmp_array[i][j][1]))
                    break
            print(curr_value)

        res.append(curr_value)
    print(res)

    return min(res)


if __name__ == '__main__':
    print(calculate(read_file()))
