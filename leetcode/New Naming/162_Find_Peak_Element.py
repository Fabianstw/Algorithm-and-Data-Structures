"""Find the Peak Element in a list"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid == 0:
                if nums[1] > nums[0]:
                    return 1
                return 0
            elif mid == len(nums) - 1:
                if nums[len(nums) - 2] > nums[len(nums) - 1]:
                    return len(nums) - 2
                return len(nums) - 1
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1



if __name__ == '__main__':
    c = Solution()
    print(c.findPeakElement([1,2]))