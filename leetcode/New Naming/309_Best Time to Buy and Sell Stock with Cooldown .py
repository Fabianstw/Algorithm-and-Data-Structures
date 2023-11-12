"""leetcode"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def helper(index, last):
            if (index, last) in cache:
                return cache[(index, last)]

            if index >= len(prices):
                return 0

            if last == 'buy':
                cache.update({(index, last): max(prices[index] + helper(index + 2, 'cls'),
                                                 helper(index + 1, 'cls'))})
                return cache[(index, last)]

            if last == 'cls':
                cache.update({(index, last): max(-prices[index] + helper(index + 1, 'buy'),
                                                 helper(index + 1, 'cls'))})
                return cache[(index, last)]

        return helper(0, 'cls')


if __name__ == '__main__':
    c = Solution()
    print(c.maxProfit([1, 2, 3, 0, 2]))
