"""Leetcode"""

from typing import List


class Solution:

    def canCross(self, stones: List[int]) -> bool:
        pass

    def canCross_rek(self, stones: List[int], lastjump=1, value=1) -> bool:

        if lastjump <= 0:
            return False

        if value == stones[-1]:
            return True

        if value in stones:
            return self.canCross_rek(stones, lastjump + 1, value + lastjump + 1) or \
                self.canCross_rek(stones, lastjump, value + lastjump) or \
                self.canCross_rek(stones, lastjump - 1, value + lastjump - 1)
        else:
            return False


if __name__ == '__main__':
    c = Solution()
    print(c.canCross([0,1,2,3,4,8,9,11]))
