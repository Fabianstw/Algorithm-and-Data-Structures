"""Remove duplicate from list"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, counter = 0, 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] == nums[i+2]:
                if nums[i] != "_":
                    nums.remove(nums[i])
                    nums.append("_")
                    counter += 1
                else:
                    break
            else:
                i += 1
        print(nums)
        return len(nums) - counter


if __name__ == '__main__':
    c = Solution()
    print(c.removeDuplicates([1, 1, 2]))
