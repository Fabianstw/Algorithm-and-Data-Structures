"""
Today: 16.11.2023
1980_Find_Unique_Binary_String
"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binary_nums = [0] * (2**(len(nums)))

        for num in nums:
            tmp = "0b" + num
            tmp = int(tmp, 2)
            binary_nums[tmp] = 1

        for i in range(len(binary_nums)):
            if binary_nums[i] == 0:
                tmp = str(bin(i))
                tmp = tmp[2:]
                if len(tmp) != len(nums[0]):
                    tmp = "0"* (len(nums[0])-len(tmp)) + tmp
                return tmp





if __name__ == '__main__':
    c = Solution()
    print(c.findDifferentBinaryString(["00","01"]))