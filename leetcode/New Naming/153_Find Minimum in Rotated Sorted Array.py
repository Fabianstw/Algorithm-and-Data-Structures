"""Find the minimum of nums in a rotated but sorted array"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            print(start, end)
            if end - start <= 2:
                return min(nums[start:end+1])
            mid = (start + end) // 2
            if nums[start] <= nums[mid] <= nums[end]:
                return nums[start]
            elif nums[start] <= nums[mid] and nums[start] >= nums[end]:
                start = mid
            elif nums[start] >= nums[mid]:
                end = mid


if __name__ == '__main__':
    c = Solution()
    print(c.findMin([4,5,6,7,0,1,2]))
