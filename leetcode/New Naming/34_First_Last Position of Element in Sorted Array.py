"""Find the index of the first and last postion of a target in nums"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            if nums[mid] == target:
                first_index = mid
                second_index = mid
                if first_index > 0:
                    while nums[first_index - 1] == target:
                        first_index -= 1
                        if first_index == 0:
                            break
                if second_index < len(nums) - 1:
                    while nums[second_index + 1] == target:
                        second_index += 1
                        if second_index == len(nums) - 1:
                            break

                return [first_index, second_index]

            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [-1, -1]


if __name__ == '__main__':
    c = Solution()
    nums = [1]
    target = 1
    print(c.searchRange(nums, target))
