import copy
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        calc = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    calc[i][j] = self.gcd(nums[i], nums[j])

        for c in calc:
            print(c)

        def helper(matrix, start, cache):

            if start < len(nums) // 2:
                get_max = 0
                col, row = [-1], [- 1]
                for i in range(len(nums)):
                    for j in range(i, len(nums)):
                        if matrix[i][j] == get_max and matrix[i][j] != 1:
                            col.append(i)
                            row.append(j)
                        if matrix[i][j] > get_max:
                            get_max = matrix[i][j]
                            col, row = [i], [j]
                if len(col) == 0:
                    for i in range(len(nums)):
                        matrix[i][row] = 0
                        matrix[row][i] = 0
                        matrix[col][i] = 0
                        matrix[i][col] = 0
                    cache += (get_max * (len(nums) // 2 - start))
                    return helper(matrix, start + 1, cache)
                else:
                    results = []
                    for index in range(len(col)):
                        new_matrix = copy.deepcopy(matrix)
                        for ind in range(len(nums)):
                            matrix[ind][row[index]] = 0
                            matrix[row[index]][ind] = 0
                            matrix[col[index]][ind] = 0
                            matrix[ind][col[index]] = 0
                        cache += (get_max * (len(nums) // 2 - start))
                        results.append(helper(new_matrix, start + 1, cache))
                        cache -= (get_max * (len(nums) // 2 - start))
                    index = results.index(max(results))
                    for ind in range(len(nums)):
                        matrix[ind][row[index]] = 0
                        matrix[row[index]][ind] = 0
                        matrix[col[index]][ind] = 0
                        matrix[ind][col[index]] = 0
                    cache += (get_max * (len(nums) // 2 - start))
                    return helper(matrix, start + 1, cache)

            else:
                return cache

        res = helper(calc, 0, 0)

        return res

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x



if __name__ == '__main__':
    c = Solution()
    print(c.maxScore([109497,983516,698308,409009,310455,528595,524079,18036,341150,641864,913962,421869,943382,295019]))