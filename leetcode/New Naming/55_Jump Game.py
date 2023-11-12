class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        res = [0 for _ in range(len(nums))]
        res[0] = 1
        for i in range(len(nums)):
            print(res)
            if res[i] == 1:
                for j in range(1, nums[i] + 1):
                    if i + j >= len(nums) - 1:
                        return True
                    res[i + j] = 1
        return False


if __name__ == '__main__':
    c = Solution()
    print(c.canJump([1, 0, 0]))
