"""
Today: 14.11.2023
45. Jump Game II
"""
from typing import List


class Solution:
    """
    Not the best runtime
    It was early
    """
    def jump(self, nums: List[int]) -> int:
        steps = [None] * len(nums)
        steps[0] = 0
        for i in range(len(nums)):
            step = nums[i]
            for j in range(step):
                if steps[-1] is not None:
                    return steps[-1]
                if steps[i + j + 1] is None:
                    steps[i + j + 1] = steps[i] + 1
                elif steps[i + j + 1] > i:
                    steps[i + j + 1] = steps[i] + 1
        return steps[-1]


if __name__ == '__main__':
    c = Solution()
    print(c.jump([1,2,1,1,1]))
