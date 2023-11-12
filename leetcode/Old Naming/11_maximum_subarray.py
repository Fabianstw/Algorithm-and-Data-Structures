"""Find the subarray in an array with the maximum sum in addition"""

from typing import List


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    middle = len(nums) // 2

    _ = maxSubArray(nums[:middle])
    _ = maxSubArray(nums[middle:])

    cross_sum = 0
    left_cross_sum = -99999
    for i in range(middle - 1, -1, -1):
        cross_sum += nums[i]
        left_cross_sum = max(cross_sum, left_cross_sum)

    cross_sum = 0
    right_cross_sum = -99999
    for j in range(middle, len(nums)):
        cross_sum += nums[j]
        right_cross_sum = max(cross_sum, right_cross_sum)

    all_cross_sum = left_cross_sum + right_cross_sum

    return max(right_cross_sum, left_cross_sum, all_cross_sum)


if __name__ == '__main__':
    print(maxSubArray([1]))
