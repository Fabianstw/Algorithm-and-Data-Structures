# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return 0

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        lheight = height(root.left)
        rheight = height(root.right)
        if self.isBalanced(root.left) is False:
            return False
        if self.isBalanced(root.right) is False:
            return False
        if abs(lheight - rheight) <= 1:
            return True
        return False


if __name__ == '__main__':
    # create a tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    c = Solution()
    print(c.isBalanced(root))
