from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = dict()
        def helper(index, last="sell"):
            if (index, last) in dp:
                return dp[(index, last)]
            if index >= len(prices):
                return 0

            if last == "buy":
                value = max(helper(index+1, "buy"), prices[index] + helper(index + 1, "sell"))
            if last == "sell":
                value = max(helper(index + 1, "sell"), -prices[index] + helper(index + 1, "buy"))
            dp.update({(index, last): value})
            return dp[(index, last)]

        return helper(0)



if __name__ == '__main__':
    c = Solution()
    print(c.maxProfit([7, 1, 5, 3, 6, 4]))