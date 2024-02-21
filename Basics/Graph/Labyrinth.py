

def read_input():
    matrix = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["|", "s", " ", "|", " ", " ", " ", " ", " ", "|"],
        ["|", " ", " ", "|", "-", "-", "-", "|", " ", "|"],
        ["|", " ", " ", " ", " ", "|", " ", " ", " ", "|"],
        ["|", "-", "-", " ", " ", " ", " ", " ", "-", "|"],
        ["|", " ", " ", " ", " ", "|", " ", " ", " ", "|"],
        ["|", " ", " ", "-", "-", "-", "-", " ", " ", "|"],
        ["|", " ", " ", "|", " ", " ", " ", " ", " ", "|"],
        ["|", " ", " ", " ", " ", " ", " ", "|", "z", "|"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ]
    return matrix


def is_there_a_solution(matrix):
    start, stack = [1, 1], [[1, 1]]
    while stack:
        current = stack.pop()
        if matrix[current[0]][current[1]] == "z":
            return True
        if matrix[current[0]][current[1]] == " " or matrix[current[0]][current[1]] == "s":
            matrix[current[0]][current[1]] = "."
            stack.append([current[0] + 1, current[1]])
            stack.append([current[0] - 1, current[1]])
            stack.append([current[0], current[1] + 1])
            stack.append([current[0], current[1] - 1])
    return False


if __name__ == '__main__':
    matrix = read_input()
    print(is_there_a_solution(matrix))