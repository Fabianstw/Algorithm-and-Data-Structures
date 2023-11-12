# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q is None and p is None:
            return True
        elif q is None and p is not None:
            return False
        elif q is not None and p is None:
            return False

        if p.val == q.val:
            if self.isSameTree(q.left, p.left) is False:
                return False
            if self.isSameTree(q.right, p.right) is False:
                return False
        else:
            return False
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    # root.left.left.left.left = TreeNode(6)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)
    root2.left.left.left.left = TreeNode(6)

    c = Solution()
    print(c.isSameTree(root, root2))
