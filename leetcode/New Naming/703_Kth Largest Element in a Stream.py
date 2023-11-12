class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        start = 0
        while start < len(self.nums) - 1:
            if self.nums[start] > val:
                self.nums.insert(start, val)
                break
            start += 1

        if start == len(self.nums):
            self.nums.append(val)

        return self.nums[len(self.nums) - self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
