"""Trapping Rain Water 42"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maximum = max(height)
        left, right, water = 0, 1, 0

        while right < len(height):

            if height[left] == maximum:
                height[left] = 0
                maximum = max(height[left+1:])
                height[left] = maximum
                if height[left] == height[left + 1]:
                    height = height[1:]
                    continue
            if height[right] >= height[left]:
                calc = height[left] * (right - left - 1)
                calc -= sum(height[left+1:right])
                water += calc
                left = right
                right += 1
                if height[left] >= max(height[left:]):
                    if left < len(height) - 1:
                        while left + 1 == right and height[left] == height[right]:
                            left += 1
                            right += 1
                            if right >= len(height) - 1:
                                return water
                        height[left] = max(height[left + 1:])
            else:
                right += 1

        return water


if __name__ == '__main__':
    c = Solution()
    print(c.trap([6,5,2,5,6,9,1,1]))

    print([1,2,3,4,5][3:])
    # First hard leetcode task
