# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -999999

        def max_wight(node):
            if not node:
                return 0
            return node.val + max(max_wight(node.left), max_wight(node.right))

        left = max_wight(root.left)
        right = max_wight(root.right)
        max_path = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
        max_lr = max(left, right, left + right + root.val, root.val, root.val + left, root.val + right)
        return max(max_path, max_lr, max_lr + max_path - root.val)


if __name__ == '__main__':
    # [9, 6, -3, null, null, -6, 2, null, null, 2, null, -6, -6, -6]
    root = TreeNode(6)
    root.left = TreeNode(9)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(2)
    root.right.right.left.left = TreeNode(-6)
    root.right.right.left.right = TreeNode(-6)
    root.right.right.left.left.left = TreeNode(-6)

    """root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)"""

    s = Solution()
    print(s.maxPathSum(root))