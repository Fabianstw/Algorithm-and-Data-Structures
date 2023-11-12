"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        start, end = 0, len(height) - 1

        while start < end:
            calc = min(height[start] * (end - start), height[end] * (end - start))
            if calc > curr_max:
                curr_max = calc
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return curr_max


if __name__ == '__main__':
    c = Solution()
    print(c.maxArea([1,8,6,2,5,4,8,3,7]))
