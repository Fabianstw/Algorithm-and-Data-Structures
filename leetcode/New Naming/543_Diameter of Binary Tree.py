# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


lass Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        return max(height(root.left) + height(root.right), self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))

if __name__ == '__main__':
    # create a complex binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)

    c = Solution()
    print(c.diameterOfBinaryTree(root))
