""""""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        result = [[0 for m in range(len(obstacleGrid[0]))] for n in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    if i == 0 or j == 0:
                        result[i][j] = 1
                    else:
                        result[i][j] = result[i-1][j] + result[i][j-1]

        return result[-1][-1]


if __name__ == '__main__':
    c = Solution()
    print(c.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
