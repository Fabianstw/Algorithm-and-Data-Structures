from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        maxi = 0

        def dfs(ind_i, ind_j):
            stack = [(ind_i, ind_j)]
            maximum = 0
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    maximum += 1
                    neighbours = [(current[0] - 1, current[1]), (current[0] + 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]
                    for neigh in neighbours:
                        if 0 <= neigh[0] < len(grid) and 0 <= neigh[1] < len(grid[0]):
                            if grid[neigh[0]][neigh[1]] == 1:
                                stack.append(neigh)
            return maximum

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    calc = dfs(i, j)
                    if calc > maxi:
                        maxi = calc

        return maxi


if __name__ == '__main__':
    c = Solution()
    print(c.maxAreaOfIsland([[0,1],[1,1]]))
