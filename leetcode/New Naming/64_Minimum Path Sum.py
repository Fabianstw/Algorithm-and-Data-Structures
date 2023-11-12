""""""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        result = [[0] * m] * n

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    result[i][j] = grid[i][j]
                elif j == 0 and i != 0:
                    result[i][j] = result[i - 1][j] + grid[i][j]
                elif j != 0 and i == 0:
                    result[i][j] = result[i][j - 1] + grid[i][j]
                else:
                    result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]

        return result[-1][-1]


if __name__ == '__main__':
    c = Solution()
    print(c.minPathSum([[1,2],[1,1]]))
