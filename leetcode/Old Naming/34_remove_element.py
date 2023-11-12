"""Remove element of list"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count_times = nums.count(val)
        for i in range(count_times):
            nums.remove(val)
            nums.append("_")

        print(nums)
        return len(nums) - count_times



if __name__ == '__main__':
    c = Solution()
    print(c.removeElement([3,2,2,3], 3))
