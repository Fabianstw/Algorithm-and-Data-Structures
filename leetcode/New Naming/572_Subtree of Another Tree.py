# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root and subRoot:

            def helper(main, sub):
                if main is None and sub is None:
                    return True
                if main is None and sub is not None:
                    return False
                if main is not None and sub is None:
                    return False
                if main.val != sub.val:
                    return False
                return helper(main.left, sub.left) and helper(main.right, sub.right)

            if helper(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        else:
            return False



if __name__ == '__main__':
    c = Solution()

    baum = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))

    print(c.isSubtree(baum, TreeNode(4, TreeNode(1), TreeNode(2))))