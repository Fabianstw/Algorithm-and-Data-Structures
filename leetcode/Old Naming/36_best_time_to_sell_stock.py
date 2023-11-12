"""adlasd"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, curr_max = 0, 1, 0
        while j < len(prices):
            price = prices[j] - prices[i]
            if price > curr_max:
                curr_max = price
                j += 1
            elif price < 0:
                i = j
            j += 1


        return curr_max


if __name__ == '__main__':
    # test
    c = Solution()
    print(c.maxProfit([1, 2, 4]))
