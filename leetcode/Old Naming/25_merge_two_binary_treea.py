"""Merge to binary trees, if nodes overlap then the sum"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_all(self):
        print(self.val)
        if self.left:
            self.left.print_all()
        if self.right:
            self.right.print_all()


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left),
                            self.mergeTrees(root1.right, root2.right))
        elif root1 and not root2:
            return TreeNode(root1.val, self.mergeTrees(root1.left, None),
                            self.mergeTrees(root1.right, None))
        elif not root1 and root2:
            return TreeNode(root2.val, self.mergeTrees(None, root2.left),
                            self.mergeTrees(None, root2.right))
        else:
            return None


if __name__ == '__main__':
    # create two trees
    tree1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    tree2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))

    s = Solution()
    new_tree = s.mergeTrees(tree1, tree2)
    new_tree.print_all()
