"""875 Koko eating Bananas Binary Search"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        if h == len(piles):
            return max_piles
        else:
            start, end = 1, max_piles
            while start < end:
                print(start, end)
                mid = (start + end) // 2
                if self.duration(piles, mid, h):
                    if end == mid or start == mid:
                        print(start, end)
                        end -= 1
                    else:
                        end = mid
                else:
                    if end == mid or start == mid:
                        start += 1
                    else:
                        start = mid

        return end

    def duration(self, piles, k, h):
        duration = 0
        for pile in piles:
            duration += math.ceil(pile / k)

        return duration <= h


if __name__ == '__main__':
    c = Solution()
    print(c.minEatingSpeed([3,6,7,11], 8))
