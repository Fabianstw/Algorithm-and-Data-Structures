"""leet"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        result = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        coins.sort()
        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount, -1, -1):
                if j == amount:
                    result[i][j] = 1
                elif j + coins[i] <= amount:
                    if i < len(coins)-1:
                        result[i][j] = result[i][j + coins[i]] + result[i+1][j]
                    else:

                        result[i][j] = result[i][j + coins[i]]

        print(result)
        return result[0][0]




if __name__ == '__main__':
    c = Solution()
    print(c.change(100, [1, 99]))
