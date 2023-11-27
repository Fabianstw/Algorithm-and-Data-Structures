"""Maximum subarray task first rekursiv then iterativ with DP"""


class Solution(object):
    def maxSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left_part = nums[:mid]
        right_part = nums[mid:]
        left_max = self.maxSubArray(left_part)
        right_max = self.maxSubArray(right_part)

        cross_sum = 0
        left_cross = -99999999
        for i in range(mid -1, -1, -1):
            cross_sum += nums[i]
            left_cross = max(cross_sum, left_cross)

        cross_sum = 0
        right_cross = -99999999
        for i in range(mid, len(nums)):
            cross_sum += nums[i]
            right_cross = max(cross_sum, right_cross)

        all_cross = left_cross + right_cross
        return max(left_max, all_cross, right_max)

    def maxSubArray(self, nums):
        res = []
        current_max = -9999999
        for i, num in enumerate(nums):
            if i == 0:
                res.append(num)
            else:
                if res[i-1] + num > num:
                    res.append(res[i-1] + num)
                else:
                    res.append(num)
            if res[i] > current_max:
                current_max = res[i]
        return current_max


if __name__ == '__main__':
    c = Solution()
    print(c.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
