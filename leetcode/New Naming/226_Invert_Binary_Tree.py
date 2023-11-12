class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        if root.left is not None:
            left_kind = self.invertTree(root.left)
        else:
            left_kind = None
        if root.right is not None:
            right_kind = self.invertTree(root.right)
        else:
            right_kind = None

        root.left = right_kind
        root.right = left_kind

        return root