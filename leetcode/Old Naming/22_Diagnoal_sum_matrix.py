"""Get the diagonal sum of a matrix"""
import math
from typing import List


def diagonalSum(mat: List[List[int]], s1=0, s2=-1) -> int:
    if s2 == -1:
        s2 = len(mat) - 1

    if s1 > len(mat) - 1:
        return 0

    res = 0
    print(s1, s2)
    if s1 == s2:
        res += mat[s1][s1] + diagonalSum(mat, s1 + 1, s2 - 1)
    else:
        res += mat[s1][s1] + mat[s1][s2] + diagonalSum(mat, s1 + 1, s2 - 1)

    return res


if __name__ == '__main__':
    print(diagonalSum([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]))
