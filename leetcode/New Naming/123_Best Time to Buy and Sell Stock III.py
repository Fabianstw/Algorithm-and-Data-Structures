from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = dict()

        def helper(index, last="sell", nt=0):
            if nt == 2:
                return 0
            if (index, last, nt) in dp:
                return dp[(index, last, nt)]
            if index >= len(prices):
                return 0

            if last == "buy":
                value = max(helper(index + 1, "buy", nt), prices[index] + helper(index + 1,"sell", nt+1))
            if last == "sell":
                value = max(helper(index + 1, "sell", nt), -prices[index] + helper(index + 1,"buy", nt))
            dp.update({(index, last, nt): value})
            return dp[(index, last, nt)]

        return helper(0)



if __name__ == '__main__':
    c = Solution()
    print(c.maxProfit([3,3,5,0,0,3,1,4]))