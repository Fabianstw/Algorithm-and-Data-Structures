"""Search target in nums (increased) but rotated"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    c = Solution()
    print(c.search(nums, target))
