"""Return the elements of a matrix in spiral order."""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    i, j = 0, 0
    for _ in range(len(matrix)):
        for _ in range(len(matrix[0])):
            if i == 0 and j < len(matrix[0]) - 1:
                result.append(matrix[i][j])
                if j + 1 < len(matrix[0]):
                    j += 1
            elif j == len(matrix[0]) - 1 and i < len(matrix):
                result.append(matrix[i][j])
                if i + 1 == len(matrix):
                    j -= 1
                else:
                    i += 1
            elif i == len(matrix) -1 and j > 0:
                result.append(matrix[i][j])
                if j - 1 >= 0:
                    j -= 1
                else:
                    i -= 1
            elif j == 0 and i > 0:
                result.append(matrix[i][j])
                if i - 1 == 0:
                    new_matrix = [row[1:-1] for row in matrix[1:-1]]
                    result.extend(spiralOrder(new_matrix))
                    return result
                else:
                    i -= 1
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix_2))
