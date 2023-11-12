class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]

        print(result)
        return result[len(result) - 1][len(result[0]) - 1]


if __name__ == '__main__':
    c = Solution()
    print(c.uniquePaths(3, 7))