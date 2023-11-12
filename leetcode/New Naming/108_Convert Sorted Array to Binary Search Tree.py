"""Convert increasing order array to BST"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid+1:])

        return head


if __name__ == '__main__':
    c = Solution()
    nums = [-10, -3, 0, 5, 9]
    a = c.sortedArrayToBST(nums)
    print(a.val)
    print(a.left.val)
    print(a.right.val)
    print(a.right.left.val)