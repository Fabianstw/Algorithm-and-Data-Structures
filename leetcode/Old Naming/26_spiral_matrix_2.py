"""
Spiral Matrix 2
Create a n*n matrix filled with the values of i^2
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 2], [4, 3]]

    if n > 2:
        res_list = [[0 for _ in range(n)] for _ in range(n)]
        bottom = 0
        left = 0
        top = n - 1
        right = n - 1
        current = 1
        while True:
            # make for loops based on top ...
            # then reduce each elemnt by one after loop
            # make 4 loop
            pass


if __name__ == '__main__':
    generateMatrix(3)
