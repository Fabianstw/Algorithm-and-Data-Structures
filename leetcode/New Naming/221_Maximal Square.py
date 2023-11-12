from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        current_max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        result[i][j] = int(matrix[i][j])
                    else:
                        minimals = [int(result[i-1][j-1]), int(result[i][j - 1]), int(result[i - 1][j])]
                        if min(minimals) == 0:
                            result[i][j] = int(matrix[i][j])
                        else:
                            current_min = min(minimals)
                            counter = 0
                            for mini in minimals:
                                if mini >= current_min:
                                    counter += 1
                            if counter == 3:
                                result[i][j] = current_min + 1
                            else:
                                result[i][j] = current_min
                    if current_max < result[i][j]:
                        current_max = result[i][j]

        return current_max ** 2


if __name__ == '__main__':
    c = Solution()
    print(c.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]))